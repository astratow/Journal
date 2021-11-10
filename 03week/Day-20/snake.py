from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
  new_segment = Turtle('square')
  new_segment.color('white')
  new_segment.penup() #//removes line
  new_segment.goto(position)
  segments.append(new_segment)

screen.update()


game_on = True

while game_on:
  screen.update()
  for seg in segments:
    seg.forward(20)
    #screen.update()
    time.sleep(1)
