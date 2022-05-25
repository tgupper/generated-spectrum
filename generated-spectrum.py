'''
This code generates generative art images based on a color gradient inspired by Ellsworth Kelly's "Spectrum".
In the same repository, you can find a version in which each step of the program is thoroughly explained,
so that people who have not written code before can easily understand it.

For more information, check out my blog post about the project: tamaragupper.de/blog

'''

__author__ = "Tamara Gupper"
__email__ = "tamara.gupper@posteo.de"

import random
import datetime
import time
import secrets
from PIL import Image, ImageDraw

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

seed = secrets.token_hex(4)
random.seed(seed)

width = 1500
height = 1000

img  = Image.new( mode = "RGB", size = (width, height), color="#FFFFFF")
draw = ImageDraw.Draw(img)

for col in range(30):
    for row in range(20):
        color_number = round((-0.2) + col*(12.5/30) + random.uniform(-0.5,0.5))
        draw.rectangle(
            (50*col, 50*row, 50*col+45, 50*row+45), 
            fill=list(colors.values())[color_number]
        )
        #draw.text(
        #    (50*col+25, 50*row+25),
        #    str(color_number),
        #    font_size=32
        #)

today = datetime.datetime.today()
timestamp = time.mktime(today.timetuple())
img.save(f"generated-spectrum-{timestamp}-{seed}-numbers.png")
