__author__ = "Skills Drift"
__copyright__ = "Copyright (C) 2021"
__version__ = "1.0"

"""
Package Instalation: pip install turtle
Source: https://docs.python.org/3/library/turtle.html#module-turtle
"""

from turtle import *

# set window configuration parameter
title("Art with code") 
setup (width=800, height=600)
bgcolor("white")
screensize(100, 400)

color('green', 'purple')

begin_fill()
while True:
    forward(200)
    left(170)
    pensize(1) # This is pen brush size 
    circle(8) # Make circle with radius 8
    speed(10) # Increase faster drawing 
    if abs(pos()) < 1:
        break
end_fill()
done()


