from math import sqrt
class animal(x, y, v):
    def __init__(self, x, y, v):
        self.position = (x, y)
        self.speed = v

def dogRel(dog, rabbit, t):
    rabbitCurrent = (rabbit.position[0], t * rabbit.speed * rabbit.position[1])
    Xdog = dog.position[0] - rabbitCurrent[0]
    Ydog = dog.position[1] - rabbitCurrent[1]
    distance = sqrt(Xdog**2 + Ydog**2)
    return ((dog.speed * Xdog) / distance , (dog.speed * Ydog) / distance)

