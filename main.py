import turtle
import sys
from random import randint

# Reset Recursion Limit
sys.setrecursionlimit(75000)

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Setup
t = turtle.Turtle()
t.speed(0)
lpb = []

pen_thickness = 5

t.pu()
t.color("black")

t.setposition(-150.0, -150.0)

# Base dots/points
for _ in range(0,3):
  lpb.append(t.position())
  t.pd()
  t.dot(pen_thickness)
  t.pu()
  t.forward(300)
  t.left(120)

# Getting the middle point coordinate between 2 points
def get_middle_point(point1=(0,0)):
  p1 = point1
  p2 = (0, 0)
  def something():
    p1 = lpb[randint(0, len(lpb)-1)] if point1 == (0,0) else point1
    p2 = lpb[randint(0, len(lpb)-1)]
    if p1 == p2:
      something()

    return p1, p2

  p1 = something()[0]
  p2 = something()[1]
  
  middle_x = (p1[0] + p2[0]) / 2
  middle_y = (p1[1] + p2[1]) / 2
  return (middle_x, middle_y)

# Main loop
def main(point1=(0,0)):
  currPoint = get_middle_point(point1)
  t.setposition(currPoint)
  t.pd()
  t.dot(pen_thickness)
  t.pu()

  if len(lpb) < 50000:
    main(currPoint)

# Start the program
main()
screen.mainloop()