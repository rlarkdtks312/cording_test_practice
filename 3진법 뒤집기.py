# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:02:57 2021

@author: kim
"""

def solution(n):
    answer = 0
    tran = ''
    
    while n:
        tran = tran + str(n%3)
        n = n // 3
        
    answer = int(tran, 3) #int base를 사용하여 특정 진수를 10 진수로 변환이 가능하다.

    return answer

n = 125
solution(n)