# raspberrypi-rc522-totp
TOTP code generator for Raspberry Pi with secrets stored on rc522 RFID tag

![screenshotMainWindow](https://user-images.githubusercontent.com/90598549/134535697-83d64e2b-03be-4632-bc80-8a2dbb2863fe.png)


## install your RC522 reader
This software is based on the library of a [blog post](https://pimylifeup.com/raspberry-pi-rfid-rc522/). Install your reader as described there.

## install depencies
* tkinter (window) `sudo apt install python3-tk`
* pyotp (totp generator) `pip3 install pyotp`

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
