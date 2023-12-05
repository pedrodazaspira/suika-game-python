from enum import Enum
import pymunk
import pymunk.pygame_util

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
redGreen = (0, 255, 255)
black = (0, 0, 0)
violent = (255, 255, 0)
grey = (200, 200, 200)
orange = (255, 0, 255)
red200 = (200, 0, 0)
green200 = (0, 200, 0)
blue200 = (0, 0, 200)
violent200 = (200, 200, 0)
orange200 = (200, 0, 200)
redGreen200 = (0, 200, 200)

class BallData:
    def __init__(self, position, space, ballType):
        self.ballType = ballType
        self.body = pymunk.Body(1, self.ballType)  # Masa e inercia
        self.body.position = (position[0], 12)
        self.shape = pymunk.Circle(self.body, self.ballType)  # Radio de la pelota
        self.validateColor()

        self.shape.elasticity = 0.3  # Elasticidad
        space.add(self.body, self.shape)
        self.space = space
        

    def validateColor(self):
        if self.ballType == 10:
            self.color = blue
            self.points = 2
        elif self.ballType == 20:
            self.color = red
            self.points = 4
        elif self.ballType == 30:
            self.color = green
            self.points = 6
        elif self.ballType == 40:
            self.color = violent
            self.points = 8
        elif self.ballType == 50:
            self.color = redGreen
            self.points = 10
        elif self.ballType == 60:
            self.color = black
            self.points = 12
        elif self.ballType == 70:
            self.color = orange
            self.points = 14
        elif self.ballType == 80:
            self.color = red200
            self.points = 16
        elif self.ballType == 90:
            self.color = green200
            self.points = 18
        elif self.ballType == 100:
            self.color = violent200
            self.points = 20
        elif self.ballType == 110:
            self.color = orange200
            self.points = 22
        elif self.ballType == 120:
            self.color = redGreen200
            self.points = 24

    def upLevel(self, space):
        self.ballType += 10
        self.shape = pymunk.Circle(self.body, self.ballType) 

        self.validateColor()

        space.add(self.shape)
        