#!/usr/bin/python
import sys
sys.argv.pop(0)

black='\033[30m'
red='\033[31m'
cyan='\036[31m'
bold='\033[1m'
underline='\033[4m'
rev='\033[7m'
reset='\033[0m'
bg_white='\033[47m'

def strip_stars(x):
    while x[0] == '*':
        x = x[1:len(x)]
    return x[1:len(x)]



for f in sys.argv:
    for i in open(f):        
        if len(i) > 2 and i[0] == '*' and i[1] == '*':
            print underline, strip_stars(i),reset,
        elif len(i) > 1 and i[0] == '*':
            print bg_white,black,bold, strip_stars(i),reset,
        else:
            print i,
        
