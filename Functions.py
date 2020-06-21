import math


class Functions:
    @staticmethod
    def happy_cat(x1, x2, x3, x4):
        vector_length_cubed = x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2
        sum_of_x = x1 + x2 + x3 + x4
        return math.fabs(vector_length_cubed - 4) ** 0.25 + 0.25 * (0.5 * vector_length_cubed + sum_of_x) + 0.5

    @staticmethod
    def griewank(x1, x2, x3, x4):
        vector_length_cubed = x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2
        multiplication = 1
        i=1
        for x in [x1, x2, x3, x4]:
            multiplication *= math.cos(x / math.sqrt(i))
            i+=1

        return 1 + vector_length_cubed / 4000 - multiplication

    @staticmethod
    def salomon(x1, x2, x3, x4):
        square_root_result = math.sqrt(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2)

        return 1 - math.cos(2 * math.pi * square_root_result) + 0.1 * square_root_result
