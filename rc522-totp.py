import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import pyotp
import pyautogui
import time
from tkinter import *

import os
notifications = False
if os.environ['XDG_CURRENT_DESKTOP'] != 'LXDE': # on Raspberry Pi OS using LXDE notifications don't work
    print("Not on LXDE - notifications work!")
    notifications = True
    import notify2


#service names for the totp labels - make sure they are the right number and in the same order like the secrets on the rfid tag!
names = ["GitHub", "Nextcloud"]

#send a code on the keyboard
def writeCode(code):
    print("I'll write it in 1 second...")
    time.sleep(1)
    print("Write", code)
    pyautogui.write(code)

    quit()

#reads a RFID tag and splits the text into codes seperated by .
def readTag():
    id, text = reader.read()

    text = text.split(".")
    return text


def createCodes(secrets):
    global warningShown, labels

    #show a warning
    Label(main, text="Attention: Since the codes are not automatically regenerated,", font=("sans-serif", 8)).grid(row=0, column=0)
    Label(main, text="they will be invalid after a maximum of 30 seconds.", font=("sans-serif", 8)).grid(row=1, column=0)
    
        
    for i in range(len(names)):
        totp = pyotp.TOTP(secrets[i])
        code = totp.now()

        labelText = names[i] + ': ' + code
        print(labelText)

        lbl = Button(main, text=labelText, font=("sans-serif", 30), command=lambda: writeCode(code))
        lbl.grid(row=2+i, column=0)



reader = SimpleMFRC522()

if notifications:
    notify2.init("Raspberry Pi RFID TOTP code generator")
    n = notify2.Notification("Raspberry Pi RFID TOTP code generator",
                         "please scan your tag to generate codes",
                         "notification-message-im"
                        )

print("please scan your tag to generate codes")

try:
    if notifications:
        n.show()
    
    secrets = readTag()

    #show tkinter window with codes
    main = Tk()
    main.title("Raspberry Pi RFID TOTP code generator")

    createCodes(secrets)

    #always in foreground
    main.call('wm', 'attributes', '.', '-topmost', '1')

    main.mainloop()

finally:
    GPIO.cleanup()