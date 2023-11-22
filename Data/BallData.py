from enum import Enum
import pymunk
import pymunk.pygame_util

class BalType(Enum):
    tipo1 = 0
    tipo2 = 1
    tipo3 = 2
    tipo4 = 3
    tipo5 = 4
    tipo6 = 5
    tipo7 = 6
    tipo8 = 7
    tipo9 = 8
    tipo10 = 9
    tipo11 = 10
    tipo12 = 11

class BallData:
    def __init__(self, position, space, ballType):
        self.body = pymunk.Body(1, 100)  # Masa e inercia
        self.body.position = (position[0], 12)
        self.ballType = ballType
        if self.ballType == BalType.tipo1:
            self.shape = pymunk.Circle(self.body, 10)  # Radio de la pelota
        elif self.ballType == BalType.tipo2:
            self.shape = pymunk.Circle(self.body, 20)  # Radio de la pelota
        elif self.ballType == BalType.tipo3:
            self.shape = pymunk.Circle(self.body, 30)  # Radio de la pelota
        elif self.ballType == BalType.tipo4:
            self.shape = pymunk.Circle(self.body, 40)  # Radio de la pelota
        elif self.ballType == BalType.tipo5:
            self.shape = pymunk.Circle(self.body, 50)  # Radio de la pelota
        elif self.ballType == BalType.tipo6:
            self.shape = pymunk.Circle(self.body, 60)  # Radio de la pelota

        self.shape.elasticity = 0.3  # Elasticidad
        space.add(self.body, self.shape)
        self.space = space
        

    def upLevel(self, space):
        if self.ballType == BalType.tipo1:
            self.ballType = BalType.tipo2
            self.shape = pymunk.Circle(self.body, 20) 
        elif self.ballType == BalType.tipo2:
            self.ballType = BalType.tipo3
            self.shape = pymunk.Circle(self.body, 30) 
        elif self.ballType == BalType.tipo3:
            self.ballType = BalType.tipo4
            self.shape = pymunk.Circle(self.body, 40) 
        elif self.ballType == BalType.tipo4:
            self.ballType = BalType.tipo5
            self.shape = pymunk.Circle(self.body, 50) 
        elif self.ballType == BalType.tipo5:
            self.ballType = BalType.tipo6
            self.shape = pymunk.Circle(self.body, 60) 
        elif self.ballType == BalType.tipo6:
            self.ballType = BalType.tipo7
            self.shape = pymunk.Circle(self.body, 70) 
        space.add(self.shape)
        