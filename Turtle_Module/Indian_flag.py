__author__ = "Anand Kumar"
__copyright__ = "Copyright (C) 2021"
__version__ = "1.0"

import turtle
from turtle import*

# initially penup()
penup()
goto(-400, 250)
pendown()

# Orange Rectangle
color("orange")
begin_fill()
forward(800)
right(90)

forward(167)
right(90)

forward(800)
end_fill()
left(90)
forward(167)

# Green Rectangle
color("green")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

# Big Blue Circle
penup()
goto(70, 0)
pendown()
color("navy")
pensize(10)
circle(70)

# Mini Blue Circles
pensize(4)
penup()
goto(-57, -8)
pendown()
color("navy")
for i in range(24):
	begin_fill()
	circle(3)
	end_fill()
	penup()
	forward(15)
	right(15)
	pendown()
	
# Small Blue Circle
penup()
goto(20, 0)
pendown()
begin_fill()
circle(22)
end_fill()
# Spokes
penup()
goto(0, 0)
pendown()
pensize(2)
for i in range(24):
	forward(60)
	backward(60)
	left(15)

# Penup() and pendown() is to start draw from new location
penup()   
goto(-70, -300)
pendown()
write("** Jai Hind. **", font=("Arial", 18, "normal"))
#to hold the
#output window
turtle.done()
