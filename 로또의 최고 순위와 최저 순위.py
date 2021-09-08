# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:52:54 2021

@author: kim
"""

def solution(lottos, win_nums):
    zero_count = 0
    count = 0
    ran_max = 0
    answer = []
    for i in lottos:
        if i == 0:
            zero_count += 1
        elif i in win_nums:
            count += 1
    ran_max = count + zero_count
    
    if ran_max == 6:
        answer.append(1)
    elif ran_max == 5:
        answer.append(2)
    elif ran_max == 4:
        answer.append(3)
    elif ran_max == 3:
        answer.append(4)
    elif ran_max == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))