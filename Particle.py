import copy
import random


class Particle:

    def __init__(self, position):
        self.position = []
        self.velocity = []
        self.position = copy.deepcopy(list(position))
        for i in range(5):
            self.velocity.append(random.uniform(-1, 1))
        self.best_position = copy.deepcopy(list(self.position))
        self.best_value = 0
