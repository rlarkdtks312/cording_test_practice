# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:03:32 2021

@author: kim
"""
import collections

def solution(participant, completion):
    answer = ''
    answer = list(collections.Counter(participant) - collections.Counter(completion))
    return answer[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))