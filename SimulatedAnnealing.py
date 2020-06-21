import math
import random
import time


class SimulatedAnnealing:
    minimum = ()
    max_temp = 10000
    alpha = 0.9999

    @staticmethod
    def minimalize_function(f, x, time_to_run):
        deadline = time.time() + time_to_run
        SimulatedAnnealing.minimum = (x, f(*x))

        SimulatedAnnealing.max_temp *= time_to_run
        SimulatedAnnealing.current_temp = SimulatedAnnealing.max_temp

        while time.time() < deadline:
            x = SimulatedAnnealing.draw_neighbour(SimulatedAnnealing.minimum[0])

            try:
                new_value = f(*x)
            except OverflowError:
                continue

            if random.random() < SimulatedAnnealing.get_probability(new_value):
                SimulatedAnnealing.minimum = (x, new_value)

            SimulatedAnnealing.current_temp *= SimulatedAnnealing.alpha

        return SimulatedAnnealing.minimum

    @staticmethod
    def draw_neighbour(x):
        for i in range(4):
            x = SimulatedAnnealing.change_x(x, random.uniform(-1.0, 1.0), i)

        return x

    @staticmethod
    def get_probability(value):
        if value < SimulatedAnnealing.minimum[1]:
            return 1
        return math.e ** ((SimulatedAnnealing.minimum[1] - value) / SimulatedAnnealing.current_temp)

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
