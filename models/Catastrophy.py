import random


class Catastrophy:
    def __init__(self, probability = 0.02):
        self.probability = probability
        
    def impact(self, value):
        
        if random.random()/value < self.probability :
            print("catastrophy occurred!")
            return random.random()
        else:
            return 1