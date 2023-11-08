#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    weighted_sum = sum(score * weight for score, weight in my_list)
    total_sum = sum(weight for _, weight in my_list)

    if total_sum == 0:
        return 0.0
    return weighted_sum / total_sum
