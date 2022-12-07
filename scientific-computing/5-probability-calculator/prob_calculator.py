import copy
import random


# Consider using the modules imported above.

class Hat:
    contents: [];

    def __init__(self, **values):
        self.contents = []
        for k, v in values.items():
            for i in range(0, v):
                self.contents.append(k)

    def set_contents(self, contents):
        self.contents = contents.copy();

    def draw(self, count: int):
        result = []
        temp_contents = self.contents;
        if count > len(temp_contents):
            return temp_contents
        for i in range(0, count):
            if len(temp_contents) <= 0:
                break;
            ran_index = (int)(random.randrange(len(temp_contents)));
            result.append(temp_contents[ran_index]);
            del temp_contents[ran_index:ran_index + 1]

        return result;


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for i in range(0, num_experiments):
        temp_contents = hat.contents.copy()
        result = hat.draw(num_balls_drawn)
        success = True
        for color, exp_count in expected_balls.items():
            # check color 's count in result
            temp_count = 0;
            for color_ball in result:
                if color_ball == color:
                    temp_count += 1
            if temp_count < exp_count:
                success = False
                break;
        if success:
            success_count += 1

        hat.set_contents(temp_contents)

    val = success_count / num_experiments;

    return val
