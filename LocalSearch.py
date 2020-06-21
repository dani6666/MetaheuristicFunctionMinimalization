import time
from random import random


class LocalSearch:
    neighbourhood_range = 100
    neighbourhood_step_multiplier = 2
    minimum = ()

    @staticmethod
    def minimalize_function(f, starting_position, time_to_run):
        deadline = time.time() + time_to_run
        x = starting_position
        found_lower = True
        temp_x = x
        temp_min = f(*x)
        LocalSearch.minimum = (temp_x, temp_min)
        while time.time() < deadline:
            if found_lower:
                x = temp_x
            else:
                x = LocalSearch.change_x(x, random.random(), random.randint(0, 3))
            for i in range(4):
                for increase_radius in [True, False]:
                    start = 1
                    for step in range(LocalSearch.neighbourhood_range):
                        if time.time() > deadline:
                            break
                        if increase_radius:
                            start *= LocalSearch.neighbourhood_step_multiplier
                        else:
                            start /= LocalSearch.neighbourhood_step_multiplier
                        try:
                            new_x = LocalSearch.change_x(x, start, i)
                            new_value = f(*new_x)
                        except OverflowError:
                            continue
                        if new_value < temp_min:
                            temp_x = new_x
                            temp_min = new_value
                        try:
                            new_x = LocalSearch.change_x(x, -start, i)
                            new_value = f(*new_x)
                        except OverflowError:
                            continue
                        if new_value < temp_min:
                            temp_x = new_x
                            temp_min = new_value
        if temp_min < LocalSearch.minimum[1]:
            LocalSearch.minimum = (temp_x, temp_min)

        return LocalSearch.minimum

    @staticmethod
    def change_x(x, step, dimension):
        if dimension == 0:
            return x[0] + step, x[1], x[2], x[3]
        if dimension == 1:
            return x[0], x[1] + step, x[2], x[3]
        if dimension == 2:
            return x[0], x[1], x[2] + step, x[3]
        if dimension == 3:
            return x[0], x[1], x[2], x[3] + step
