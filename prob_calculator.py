import copy
import random

class Hat:
    def __init__(self, **colors):
        self.contents = list()

        for color in colors:
            for ball in range(colors[color]):
                self.contents.append(color)

    def draw(self, number):
        balls_to_draw = random.sample(self.contents, number)

        if balls_to_draw <= self.contents:
            for ball in copy.copy(self.contents):
                if ball in balls_to_draw:
                    self.contents.remove(ball)

        return balls_to_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return 0