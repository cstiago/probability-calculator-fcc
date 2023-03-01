import copy
import random

class Hat:
    def __init__(self, **colors):
        self.contents = list()

        for color in colors:
            for ball in range(colors[color]):
                self.contents.append(color)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return 0