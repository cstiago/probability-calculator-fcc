import copy
import random

class Hat:
    def __init__(self, **colors):
        self.contents = list()

        for color in colors:
            for ball in range(colors[color]):
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents

        balls_drawn = list()

        for i in range(num_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls_drawn.append(ball)

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return 0