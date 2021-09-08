# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:01:44 2021

@author: kim
"""

def solution(s):
    
    answer = ''
    s = s.replace('one', '1')
    s = s.replace('zero', '0')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    answer = s
    return int(answer)

s = "one4seveneight"

print(solution(s))
