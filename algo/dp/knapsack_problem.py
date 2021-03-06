#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-11-22 10:15

"""
Knapsack Problem.

Variants:
    1. 0/1 Knapsack
    2. 0/1 Knapsack with repetition (multiple copies of items)
    3. Knapsack with fractional items and their values
Terminologies:
    - Knapsack Capacity/Size: C/S
    - Total Items: N
    - Items Weight: w
    - Items Value: v
    - Item #: i
    - Current Knapsack Size = j
    - Candidancy of items = x
Approach:
    1. Dynamic Programming
Time Complexity:
    - Using DP: polynomial time O(S.N)
    - Using Brute Force: O(2^N)
Recurrence Relation:
    K[i,j] = max{K[i-1, j], K[i-1,w[i]-j] + v[i]}
    where 
        - K is memo table
        - i is item number
        - j is the selected weight for which calculation is going on
        - w[i] is weight of ith item 
        - v[i] is value of ith item

Application:
    - Cost/Value optimization
References:
    - https://www.youtube.com/watch?v=nLmhmB6NzcM
    - https://www.utdallas.edu/~scniu/OPRE-6201/documents/DP3-Knapsack.pdf
"""


# from pprint import pprint


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"


class Algorithm:
    """0/1 Knapsack Algorithm."""

    def __init__(self, S, N, v, w):
        self._S = S
        self._N = N
        self._v = v
        self._w = w
        self._x = [0 for _ in range(N)]  # selection of items
        self._memo_table = [[0 for _ in range(S + 1)] for _ in range(N + 1)]

    # def _compute_0_1_knapsack(self):
    #     temp = []
    #     pprint(self._memo_table)
    #     for j in range(1, self._S + 1):
    #         for i in range(1, self._N + 1):
    #             remaining_weight = (
    #                 j - self._w[i - 1] if j - self._w[i - 1] >= 0 else 0
    #             )
    #             temp.append(
    #                 self._v[i - 1] + self._memo_table[i][remaining_weight]
    #             )
    #         self._memo_table[i][j] = max(temp)
    #     pprint(self._memo_table)
    #     return self._memo_table[self._N][self._S]

    def _compute_0_1_knapsack(self):
        # pprint(self._memo_table)
        for i in range(1, self._N + 1):
            for j in range(1, self._S + 1):
                if self._w[i - 1] > j:
                    current_val = self._memo_table[i - 1][j]
                else:
                    remaining_weight = (
                        self._memo_table[i - 1][j - self._w[i - 1]]
                        if j - self._w[i - 1] >= 0
                        else 0
                    )
                    current_val = self._v[i - 1] + remaining_weight
                self._memo_table[i][j] = max(
                    self._memo_table[i - 1][j], current_val
                )
        # pprint(self._memo_table)
        max_val = self._memo_table[self._N][self._S]

        #
        # trace back to find selected items
        #
        i = self._N
        j = self._S
        value = self._memo_table[self._N][self._S]
        while value > 0:
            if self._memo_table[i][j] == self._memo_table[i - 1][j]:
                i -= 1
            else:
                self._x[i - 1] = 1  # -1 for index
                value -= self._v[i - 1]  # -1 for index
                j = self._memo_table[i - 1].index(value)
                i -= 1

        return (max_val, self._x)


def knapsack_01(S, N, v, w):
    """Solve 0/1 Knapsack Problem (without repetition).

    :param S: Int<Size of knapsack>
    :param N: Int<Number of items>
    :param v: List<Int Values of each items>
    :param w: List<Int Weights of each items>
    """
    return Algorithm(S, N, v, w)._compute_0_1_knapsack()


# print(knapsack_01(8, 4, [1, 2, 5, 6], [2, 3, 4, 5]))
