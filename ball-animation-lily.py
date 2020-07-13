# link to project on trinket
# https://trinket.io/library/trinkets/d00d7dbb26
from processing import *
import random, math


def setup():
  frameRate(30)
  size(600, 400)
  noStroke()


def mouseClicked():
  #check if it was within any balls
  number_of_balls = len(gs.balls_x)
  for index in range(number_of_balls):
    if pointInCircle(mouse.x, mouse.y, gs.balls_x[index], gs.balls_y[index], gs.balls_size[index]):
      #half the size
      gs.balls_size[index] = gs.balls_size[index]/2

      #change the direction
      gs.balls_speed_x[index] = randomDirection()
      gs.balls_speed_y[index] = randomDirection()

      #add a new ball
      newBall(gs.balls_x[index], gs.balls_y[index], gs.balls_size[index])



#changing variables
class gameState:
  balls_x = []
  balls_y = []
  balls_speed_x = []
  balls_speed_y = []
  balls_size = []
gs = gameState()


#non-changing variables


def randomDirection():
  return random.random() * random.randint(-3, 3)


def newBall(x, y, size):
  gs.balls_x.append(x)
  gs.balls_y.append(y)
  gs.balls_size.append(size)
  gs.balls_speed_x.append(randomDirection())
  gs.balls_speed_y.append(randomDirection())
newBall(300, 200, 320)


def moveEverything():
  #have to remember to delete from list after loop
  to_be_removed = []

  number_of_balls = len(gs.balls_x)
  for index in range(number_of_balls):
    #move each ball
    gs.balls_x[index] = gs.balls_x[index] + gs.balls_speed_x[index]
    gs.balls_y[index] = gs.balls_y[index] + gs.balls_speed_y[index]

    #make it appear on other side
    if gs.balls_y[index] > 420:
      gs.balls_y[index] = -20
    if gs.balls_y[index] < -20:
      gs.balls_y[index] = 420
    if gs.balls_x[index] > 620:
      gs.balls_x[index] = -20
    if gs.balls_x[index] < -20:
      gs.balls_x[index] = 620


def draw():
  moveEverything()

  background(0, 0, 0)

  fill(255, 255, 255)
  #draw each ball
  number_of_balls = len(gs.balls_x)
  for index in range(number_of_balls):
    ellipse(gs.balls_x[index], gs.balls_y[index], gs.balls_size[index], gs.balls_size[index])


def pointInCircle(pt_x, pt_y, circle_x, circle_y, circle_radius):
  dist = math.sqrt( (pt_x - circle_x)**2 + (pt_y - circle_y)**2 )
  if dist < circle_radius:
    return True
  else:
    return False



run()
