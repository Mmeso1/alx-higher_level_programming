#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    loi = list_of_integers
    loil = len(loi)
    if (loil == 0):
        return None
    else:
        mid = int(loil / 2)
        if ((mid == 0 or loi[mid - 1] <= loi[mid]) and
                (mid == loil - 1 or loi[mid + 1] <= loi[mid])):
            return loi[mid]
        elif (mid > 0 and loi[mid - 1] > loi[mid]):
            return find_peak(loi[0:mid])
        else:
            return find_peak(loi[(mid + 1):])
