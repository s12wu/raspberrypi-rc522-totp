# raspberrypi-rc522-totp
TOTP code generator for Raspberry Pi with secrets stored on rc522 RFID tag

The secrets are stored in PLAIN TEXT on your RFID tag!

Not under development anymore.

![totpScreenshot](https://user-images.githubusercontent.com/90598549/134674451-96f7f653-550b-491d-a8c6-fc62a4c356c7.png)


## install your RC522 reader
This software is based on the library of a [blog post](https://pimylifeup.com/raspberry-pi-rfid-rc522/). Install your reader as described there.

## install dependencies
* tkinter (window) `sudo apt install python3-tk`
* pyotp (totp generator), notify2 (desktop notifications) and pyautogui (keyboard input) `pip3 install pyotp notify2 pyautogui`

## write your secrets to the tag
Every application has its base32-encoded secret string. Use the Write.py from the example to write write your secrets to the tag: `SECRET1.SECRET2.`
Use es many secrets as you want, they just have to fit on the card.

```
$ python3 Write.py 
Hello World!
New Data: XXXXXXXXXXXX.XXXXXXXXXXXX.
Now place your tag to write
Written
```

## use it
Then download rc522-totp.py from this repo.
Change the line `names = ["GitHub", "Nextcloud"]` and enter the names of the applications you used (in the right order).
Then run it with `python3 rc522-totp.py`

Scan your tag and the codes wil appear. If you click on a code, the program will enter it on your keyboard after 1 second. While this second you can focus the input box where you have to type the code.
On Raspberry Pi OS (LXDE), notifications won't work. (I'm using Cinnamon on my Pi 4).

You can create a menu item to find it easily.
