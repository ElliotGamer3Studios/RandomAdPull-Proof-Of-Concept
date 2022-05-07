from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from string import ascii_letters
import io as io
import urllib.request
import time as timer
import random as rand
import webbrowser as webbrowser

from auth import *
import constants as constant

master = Tk() #creates the master tk object
master.title("Random Ad Pull") #changes the title
master.geometry("200x200") #size of master window
icon = PhotoImage(file="icon.png")
master.wm_iconphoto(True, icon) #change the icon
nonce = ''.join(rand.choice(ascii_letters) for i in range(18))
images = [] #required to maintain refrence to the images that are open

#url that opens the url given on creation when called
class redirectURL:

    def __init__(self, URL):
        self.URL = URL

    def __call__(self):
        webbrowser.open_new(self.URL)

#callback function that is used to get a random ad from local images
def randomAd():
    tempLocation = get_random_image()
    adWidth, adHeight = get_image_size(tempLocation)
    make_ad_window('Ad', tempLocation, adWidth, adHeight) #make the ad window appear

#callback function to get a random ad from urls
def randomAdURL():
    imageUrl = get_random_image_URL()
    make_ad_window_url('Ad Url', imageUrl, constant.DEFAULT_REDIRECT_URL)

#converts dim to geometry string or returns default
def convert_to_geometry_string(width,height):
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        return str(width)+"x"+str(height)
    return constant.DEFAULT_DIM

#get a random local image callback(currently not random because IDK how the adware images are stored)
def get_random_image():
    return constant.DEFAULT_LOCATION

#get a random image URL callback(currently not random  because IDK how the adware images are stored)
def get_random_image_URL():
    return constant.DEFAULT_URL

def get_image_from_url(imageUrl):
    raw = urllib.request.urlopen(imageUrl).read() #get the image
    img = Image.open(io.BytesIO(raw)) #read the image
    imgWidth, imgHeight = img.width, img.height #get the dims
    image = ImageTk.PhotoImage(img) #make the image
    images.append(image) #add to images
    return image, imgWidth, imgHeight #return image and dims

#get the dims of a local image using PIL
def get_image_size(imagePath):
    image = Image.open(imagePath)
    return image.width, image.height

#makes an ad window from a url
def make_ad_window_url(title = constant.DEFAULT_TITLE, location = constant.DEFAULT_URL, onClickURL = None):
    window = Toplevel(master) #get a window
    window.title(title) #set the title
    img, width, height = get_image_from_url(location) #make the image that will be added
    if width != None and height != None:
        windowSize = convert_to_geometry_string(width, height) #convert the window size
        window.geometry(windowSize) #set the geometry
    canvas = Canvas(window,width=width,height=height) #make the canvas
    canvas.pack() #pack the canvas
    canvas.create_image(0,0,anchor=NW,image=img) #create the image
    # if onClickURL != None:
    #     onClick = redirectURL(onClickURL)
    #     moreInfo = Button(window,text='Learn More',command=onClick,height=10,width=20,relief=SOLID,font=('arial', 18)) #open the onClickURL On Click
    #     moreInfo_canvas = canvas.create_window(100,200,anchor=NW,window=moreInfo)
    window.mainloop() #run the popup window loop

#creates a new window with an ad
def make_ad_window(title = constant.DEFAULT_TITLE, location = constant.DEFAULT_LOCATION, width = None, height = None):
    window = Toplevel(master) #get a window
    window.title(title) #set the title
    if width != None and height != None:
        windowSize = convert_to_geometry_string(width, height) #convert the window size
        window.geometry(windowSize) #set the geometry
    canvas = Canvas(window,width=width,height=height) #make the canvas
    canvas.pack() #pack the canvas
    img = PhotoImage(file=constant.DEFAULT_LOCATION) #make the image that will be added
    canvas.create_image(0,0,anchor=NW,image=img) #create the image
    window.mainloop() #run the popup window loop
    timer.sleep(20) #sleep for 20 seconds
    window.destroy() #destroy the window

button = Button(master,text="testAd",command=randomAdURL) #button for running a test url ad
button.pack(pady=10) #pack the button

mainloop() # run the main loop