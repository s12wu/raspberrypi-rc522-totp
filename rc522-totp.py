import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import pyotp

from tkinter import *

#service names for the totp labels - make sure they are the right number and in the same order like the secrets on the rfid tag!
names = ["GitHub", "Nextcloud"]

#reads a RFID tag and splits the text into codes seperated by .
def readTag():
    id, text = reader.read()

    text = text.split(".")
    return text

#list of tkinter label objects showing the service name with totp code
labels = []

# True after first read - no need th re-draw warning then
warningShown = False

def createCodes():
    global warningShown, labels

    #remove old codes from the window
    for i in range(len(labels)):
        labels[i].grid_forget()

    labels = []

    #show a warning
    if not warningShown:
        warningShown = True
        Label(main, text="Attention: Since the codes are not automatically regenerated,", font=("sans-serif", 8)).grid(row=1, column=0)
        Label(main, text="they will be invalid after a maximum of 30 seconds.", font=("sans-serif", 8)).grid(row=2, column=0)
    
    
    secrets = readTag();
    
    for i in range(len(names)):
        totp = pyotp.TOTP(secrets[i])
        code = totp.now()

        labelText = names[i] + ': ' + code
        print(labelText)

        lbl = Label(main, text=labelText, font=("sans-serif", 30))
        lbl.grid(row=3+i, column=0)



reader = SimpleMFRC522()
main = Tk()
main.title("Raspberry Pi RFID TOTP code generator")


try:
    Button(main, text="READ", command=createCodes).grid(row=0, column=0)
    main.mainloop()

finally:
    GPIO.cleanup()