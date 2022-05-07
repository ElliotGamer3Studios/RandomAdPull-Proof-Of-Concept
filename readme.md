# Random Ad Pull

This script pulls an image from a url or local file and opens it in a window.
It is in a proof of concept stage with the end goal of having the image displayed be a random image from the adware submissions database.

I have no good way to test the twitch intergration, so it likely will not work. If it does
the information in auth.py will need to be filled out.

Also at the moment the random url image is a picture of dice from wikipedia because I don't know how the adware-submissions images are stored.

To run the proof of concept/test run using the following command:

`python randomAdPull.py`

To run the twitch point redeem use the following command:

`python twitchEventDispacter.py`

# Required Dependences

PIL `pip install pillow`
tkinter `pip install tkinter`
flask `pip install flask`
twitchAPI `pip install twitchAPI`
