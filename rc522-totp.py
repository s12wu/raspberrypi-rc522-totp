import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import pyotp

import notify2

from tkinter import *

#service names for the totp labels - make sure they are the right number and in the same order like the secrets on the rfid tag!
names = ["GitHub", "Nextcloud"]

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

        lbl = Label(main, text=labelText, font=("sans-serif", 30))
        lbl.grid(row=2+i, column=0)



reader = SimpleMFRC522()
notify2.init("Raspberry Pi RFID TOTP code generator")

n = notify2.Notification("Raspberry Pi RFID TOTP code generator",
                         "please scan your tag to generate codes",
                         "notification-message-im"
                        )


try:
    n.show()
    
    secrets = readTag()

    #show tkinter window with codes
    main = Tk()
    main.title("Raspberry Pi RFID TOTP code generator")

    createCodes(secrets)

    main.mainloop()

finally:
    GPIO.cleanup()