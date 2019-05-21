#!/usr/local/bin/python3
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
font_bold_big = ImageFont.truetype("Arial Bold.ttf", int(font_size*1))


draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, size_x, size_y), fill='#000000', outline=None)

k = 200
x = 100
for f in sys.argv:
    for i in open(f):
        if len(i) > 2 and i[0] == '*' and i[1] == '*':
            draw.text((x, k), strip_stars(i), (0,0,0), font=font_bold)
            k += font_size * 1.2
        elif len(i) > 1 and i[0] == '*':
            draw.rectangle((x, k, x + 400, k + font_size * 1.3), fill='#222222', outline=None)
            draw.line((x, k, x + 400, k), fill='#042037', width=3)
            draw.text((x, k), strip_stars(i), fill='#ffffff',font=font_bold_big)
            k += font_size * 1.4
        else:
            draw.text((x, k), i, font=font,fill='#ffffff')
            k += font_size * 1.2
        if k > size_y * 0.75:
            x += 500
            k = 200
        
image.save("/Users/jmouret/todo/todo.png")
