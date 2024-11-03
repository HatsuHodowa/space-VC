import random


class Catastrophy:
    def __init__(self, probability = 0.1):
        self.probability = probability
        
    def impact(self, value):
        return random.random() if random.random()*value < self.probability else 1