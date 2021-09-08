# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:52:00 2021

@author: kim
"""

def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes), 1):
        if signs[i] == True:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]
    return answer

absolutes = [ 4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))

