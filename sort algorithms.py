"""
This file contain sorting algorithms and its purpose
is to use as a tool for other projects.
"""


def BubbleSort(lst):
    """
    This function implements the most primitive bubble sort algorithm.
    :param lst: list of comparable items.
    :return: sorted list of the same items.

    run time complexity = O(n^2)
    """

    n = len(lst)

    for index1 in range(n):

        for index2 in range(0, n - index1 - 1):

            # To make the sort in revers change the operator '>' to '<'.
            if lst[index2] > lst[index2 + 1]:
                lst[index2], lst[index2 + 1] = lst[index2 + 1], lst[index2]

    return lst


def OptimizedBubbleSort(lst):
    """
    This function implements the optimized bubble sort algorithm.
    its mean that the algorithm will stop iterate the list once it sorted.
    :param lst: list of comparable items.
    :return: sorted list of the same items.

    run time complexity = O(n^2)
    """

    n = len(lst)

    for index1 in range(n):
        change = 0
        for index2 in range(0, n - index1 - 1):

            # To make the sort in revers change the operator '>' to '<'.
            if lst[index2] > lst[index2 + 1]:
                lst[index2], lst[index2 + 1] = lst[index2 + 1], lst[index2]
                change = 1

        if change == 0:
            return lst

    return lst


def SelectionSort(lst):
    """
    This function implements the selection sort algorithm.
    :param lst: Unsorted list contains comparable items.
    :return: Sorted list of the same items.

    run time complexity = O(n^2)
    """
    n = len(lst)

    for index1 in range(n):
        min_index = index1

        for index2 in range(index1 + 1, n):
            if lst[index2] < lst[min_index]:
                min_index = index2

        lst[index1], lst[min_index] = lst[min_index], lst[index1]

    return lst


def InsertionSort(lst):
    """
    This function implements the selection sort algorithm.
    :param lst: Unsorted list contains comparable items.
    :return: Sorted list of the same items.

    run time complexity = O(n^2)
    """
    n = len(lst)

    for index1 in range(1, n):

        key = lst[index1]
        index2 = index1 - 1

        while index2 >= 0 and key < lst[index2]:

            lst[index2 + 1] = lst[index2]
            index2 -= 1

        lst[index2 + 1] = key

    return lst
