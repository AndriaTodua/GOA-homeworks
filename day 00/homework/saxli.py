from turtle import *

#we want to paint a house 

#step 1: draw a square
speed(30)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

#end of door

#drawing the roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of the roof

#drawing the windows

penup()
goto(30, 160)
pendown()
color("lightblue")
begin_fill()
left(120)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

end_fill()

penup()
color("black")
goto(50, 160)
pendown()
right(180)
forward(40)
penup()
goto(30,140)
pendown()
left(90)
forward(40)


penup()
goto(130, 160)
pendown()
color("lightblue")
begin_fill()
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

end_fill()

penup()
color("black")
goto(150, 160)
pendown()
left(180)
forward(40)
penup()
goto(130, 140)
pendown()
left(90)
forward(40)

exitonclick()
 