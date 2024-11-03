import random


class Catastrophy:
    def __init__(self, probability = 0.01):
        self.probability = probability
        
    def impact(self, value):
        if value == 0:
            return 1
        
        if random.random()/value < self.probability :
            print("catastrophy occurred!")
            return random.random()*0.5+0.5
        else:
            return 1