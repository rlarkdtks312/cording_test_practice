# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:40:04 2021

@author: kim
"""

def solution(N, stages):
    fail_rate = []
    arrival = []
    answer = []

    for i in range(N):
        fail_rate.append(0)
        arrival.append(0)
        
    for j in range(len(stages)):
        if stages[j] <= N:
            fail_rate[stages[j]-1] +=1
            for e in range(stages[j]):
                arrival[e] = arrival[e] + 1
        else:
            for k in range(len(arrival)):
                arrival[k] = arrival[k] + 1
                
    for f in range(N):
        try:
            fail_rate[f] = fail_rate[f] / arrival[f]
        except:
            fail_rate[f] = 0

    for t in range(N):
        answer.append(fail_rate.index(max(fail_rate))+1)
        fail_rate[fail_rate.index(max(fail_rate))] = -1
    return answer
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))