import math


def shift_variations_count(workers_list, shift_count):

    return math.factorial(len(workers_list))/(math.factorial(shift_count)*(math.factorial(len(workers_list) - shift_count)))
