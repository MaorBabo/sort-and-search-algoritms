"""
This file contain sorting algorithms and its purpose
is to use as a tool for other projects.
"""
import random


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


def Merge(lst1, lst2):
    """
    This function implement the merge algorithm
    as a helper function to MergeSort.
    :param lst1: Sorted list of comparable items.
    :param lst2: Sorted list of comparable items.
    :return: A single sorted list that contains the items from lst1 and lst2.

    run time complexity O(max(len(lst1), len(lst2)))
    """
    result = []
    index1 = index2 = 0

    while index1 < len(lst1) and index2 < len(lst2):

        if lst1[index1] <= lst2[index2]:
            result.append(lst1[index1])
            index1 += 1

        else:
            result.append(lst2[index2])
            index2 += 1

    result += lst1[index1:]
    result += lst2[index2:]

    return result


def MergeSort(lst):
    """
    This function implement the Merge sort algorithm.
    :param lst: Unsorted list of comparable items
    :return: Sorted list of the same items.

    run time complexity = O(n*log(n))
    (n = len(lst))
    """

    # Base case(the list contain just one or less items):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2

    left = MergeSort(lst[:mid])
    right = MergeSort(lst[mid:])

    return Merge(left, right)


def QuickSort(lst):
    """
    This function implement the quick
    sort algorithm using thr module "random".
    :param lst: Unsorted list of comparable items.
    :return: sorted list of the same items.

    Run time complexity:

    n = len(lst)
    worst case - O(n^2)
    best case - O(n*log(n))
    average case - O(n*log(n))

    * Usually This algorithm works with O(n*log(n)).
    """

    # Base case:
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst)

        smaller = [element for element in lst if element < pivot]
        equal = [element for element in lst if element == pivot]
        grater = [element for element in lst if element > pivot]

        return QuickSort(smaller) + equal + QuickSort(grater)




