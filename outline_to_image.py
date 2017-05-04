#!/usr/bin/python
import sys
# see http://pillow.readthedocs.io/en/4.1.x/handbook/tutorial.html
from PIL import Image
from PIL import Image, ImageDraw, ImageFont

sys.argv.pop(0)

def strip_stars(x):
    while x[0] == '*':
        x = x[1:len(x)]
    return x[1:len(x)]

size_x = 2560
size_y = 1440
image = Image.new('RGB', (2560, 1440))
image = image.point(lambda i: 255)

font_size = 25
font = ImageFont.truetype("Arial.ttf", font_size)
font_bold = ImageFont.truetype("Arial Bold.ttf", font_size)
font_bold_big = ImageFont.truetype("Arial Bold.ttf", int(font_size*1.2))


draw = ImageDraw.Draw(image)

k = 200
x = 100
for f in sys.argv:
    for i in open(f):
        if len(i) > 2 and i[0] == '*' and i[1] == '*':
            draw.text((x, k), strip_stars(i), (0,0,0), font=font_bold)
            k += font_size * 1.2
        elif len(i) > 1 and i[0] == '*':
            draw.rectangle((x, k, x + 300, k + font_size * 1.3), fill='#CCCCDD', outline=None)
            draw.line((x, k, x + 300, k), fill='#0000AA', width=3)
            draw.text((x, k), strip_stars(i), (0,0,0), font=font_bold_big)
            k += font_size * 1.4
        else:
            draw.text((x, k), i, (0,0,0), font=font)
            k += font_size * 1.2
        if k > size_y * 0.75:
            x += 400
            k = 200
        
image.save("/Users/jmouret/todo/todo.png")
