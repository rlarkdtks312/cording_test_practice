# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:41:20 2021

@author: kim
"""

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer = answer + '수'
        else:
            answer = answer + '박'
    return answer

n = 4
solution = solution(n)
print(solution)


