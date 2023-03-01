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
    success_count = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        expected_balls_copy = copy.deepcopy(expected_balls)

        success = True

        for ball in expected_balls_copy.keys():
            if balls_drawn.count(ball) < expected_balls_copy[ball]:
                success = False
                break
            else:
                balls_drawn.remove(ball)

        if success:
            success_count += 1

    probability = success_count / num_experiments

    return probability
