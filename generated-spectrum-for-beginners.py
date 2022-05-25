'''
This code generates generative art images based on a color gradient inspired by Ellsworth Kelly's "Spectrum".
I have excessively commented the code in this file specifically to allow people who have not programmed 
before to understand what each line of code does. There is another file in the same repository which
does not contain these thorough explanations. If you haven't executed a python script before, 
try this tutorial: https://pythonbasics.org/execute-python-scripts/

For more information, check out my blog post about the project: tamaragupper.de/blog

'''

__author__ = "Tamara Gupper"
__email__ = "tamara.gupper@posteo.de"

## In these first five lines, libraries are imported. Importing libraries means 
## that we can access pieces of code that others have previously written, and
## that we do not have to come up with ourselves.

import random
import datetime
import time
import secrets
from PIL import Image, ImageDraw

## This part of the code specifies the color values used in the image
## The color gradient is inspired by Ellsworth Kelly's "Spectrum".

colors={
    269:(244,215,77), #colour1
    605:(100,186,175), #colour2
    615:(1,162,167), #colour3
    999:(2,139,121), #colour4
    572:(0,112,175), #colour5
    570:(50,91,181), #colour6
    568:(113,71,145), #colour7
    344:(150,73,107), #colour8
    567:(183,57,84), #colour9
    315:(220,55,53), #colour10
    398:(245,80,48), #colour11
    276:(254,175,20), #colour12
    274:(250,220,88), #colour13
}

## The next two lines set a seed, which is a number used to reproduce the same output of
## code even if some aspects of it were produced with the random function.
## If you want to produce the image you can see in my blog post, set the seed to "d8fd0226"
## (To do that, just remove the # before the word "seed")

seed = secrets.token_hex(4)
#seed = "d8fd0226"
random.seed(seed)

## These two lines define the width and height of the generated image. You can change them to
## generate smaller or larger images.

width = 1500
height = 1000

## This line states which variables define the image. In our case, the image is based on 
## the Red-Green-Blue (RGB) color scheme, the width and height defined above, and it is initially
## completely white (which is what "FFFFFF" stands for).

img  = Image.new( mode = "RGB", size = (width, height), color="#FFFFFF")

## This line defines what should happen when we use "draw" further below - namely take the image
## we just defined and use the function ImageDraw provided by an imported library.

draw = ImageDraw.Draw(img)

## In this for-loop, every square (which is every row in every column) is assigned a color value.
## The line starting with "color_number" calculates this color value by mulitplying the column
## number with (12.5/30) and adding a random value between (-0.5) and (0.5). It also adds (-0.2)
## to make the colors at the left and right margins more balanced. This line is where you can
## get creative with the colors of the squares, so feel free to experiment!

for col in range(30):
    for row in range(20):
        color_number = round((-0.2) + col*(12.5/30) + random.uniform(-0.5,0.5))
        draw.rectangle(
            (50*col, 50*row, 50*col+45, 50*row+45), 
            fill=list(colors.values())[color_number]
        )
        ## The following five lines of code add the number of the assigned color to each square.
        ## This makes it easier to use the image as a template. Uncomment the next lines if you 
        ## also want to use it as such!

        #draw.text(
        #    (50*col+25, 50*row+25),
        #    str(color_number),
        #    font_size=32
        #)

## These three lines define the name of the file in which the generated image is saved, and save it
## in the same folder as the Python file.

today = datetime.datetime.today()
timestamp = time.mktime(today.timetuple())
img.save(f"generated-spectrum-{timestamp}-{seed}-numbers.png")
