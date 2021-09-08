# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:11:26 2021

@author: kim
"""
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for num in course:
        temp= []
        for order in orders:
            combi = combinations(sorted(order), num)
            temp += combi
        counter = Counter(temp)
        ans_temp = ''
        if len(counter) != 0 and max(counter.values()) != 1:
            for n in counter:
                if counter[n] == max(counter.values()):
                    ans_temp = ''.join(n)
                    answer += [ans_temp]
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))