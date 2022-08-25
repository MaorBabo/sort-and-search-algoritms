"""
This file contain search algorithms and its purpose
is to use as a tool for other projects.
"""


def sequentialSearch(sorted_lst, num):
    """
    This function implement sequential search on sorted list.
    :param sorted_lst: A list of numbers.
    :param num: Some number (can be of any type).
    :return: The index of the number in the list
    or -1 if the number is not in the list.

    complexity = O(len(sorted_lst))
    """

    for index in range(len(sorted_lst)):
        if sorted_lst[index] == num:
            return index

    return -1


def binarySearch(sorted_lst, num):
    """
    This function implements binary search on sorted list.
    :param sorted_lst: A list of numbers.
    :param num: Some number (can be of any type).
    :return: The index of the number in the list
    or -1 if the number is not in the list.

    run time complexity = O(log(len(sorted_lst)))
    """

    start = 0
    end = len(sorted_lst) - 1
    mid = 0

    while start <= end:

        mid = (start + end) // 2

        if sorted_lst[mid] > num:
            end = mid - 1

        elif sorted_lst[mid] < num:
            start = mid + 1

        else:
            return mid

    return -1


def recursiveBinarySearch(sorted_lst, start, end, num):
    """
    This function implements binary search in a recursive approach.
    :param sorted_lst: A list of numbers.
    :param start: The first index in the list.
    :param end: The last index in the list.
    :param num: Some number (can be of any type).
    :return: The index of the number in the list
    or -1 if the number is not in the list.

    run time complexity = O(log(len(sorted_lst)))
    """
    if end >= start:

        mid = (start + end) // 2

        if sorted_lst[mid] == num:
            return mid

        elif sorted_lst[mid] > num:
            return recursiveBinarySearch(sorted_lst, start, mid - 1, num)

        elif sorted_lst[mid] < num:
            return recursiveBinarySearch(sorted_lst, mid + 1, end, num)
    else:
        return -1

