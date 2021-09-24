# raspberrypi-rc522-totp
TOTP code generator for Raspberry Pi with secrets stored on rc522 RFID tag

![totpScreenshot](https://user-images.githubusercontent.com/90598549/134674451-96f7f653-550b-491d-a8c6-fc62a4c356c7.png)


## install your RC522 reader
This software is based on the library of a [blog post](https://pimylifeup.com/raspberry-pi-rfid-rc522/). Install your reader as described there.

## install depencies
* tkinter (window) `sudo apt install python3-tk`
* pyotp (totp generator) and notify2 (desktop notifications) `pip3 install pyotp notify2`

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

You can create a menu item to find it easily.
