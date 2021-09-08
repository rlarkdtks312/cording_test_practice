# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:07:37 2021

@author: kim
"""

def solution(n, arr1, arr2):
    answer = []
    binary_arr1 = []
    binary_arr2 = []
    
    for q in range(0, n, 1):
        answer.append('')
        
    for i in range(0, n, 1):
        binary_arr1.append(bin(arr1[i])[2:].zfill(n))
        binary_arr2.append(bin(arr2[i])[2:].zfill(n))

    for j in range(0, len(binary_arr1), 1):
        for k in range(0, n, 1):
            if binary_arr1[j][k] == '0' and binary_arr2[j][k] == '0':
                answer[j] = answer[j] + ' '
            else:
                answer[j] = answer[j] + '#'

    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
solution(n, arr1, arr2)
