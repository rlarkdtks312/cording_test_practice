# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:07:31 2021

@author: kim
"""

def solution(answers):
    first = [1, 2, 3, 4, 5] #5개 숫자로 패턴화
    second = [2, 1, 2, 3, 2, 4, 2, 5] #8
    third = [3,3,1,1,2,2,4,4,5,5] #10
    score = [0,0,0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            score[0] += 1
        if answers[i] == second[i % 8]:
            score[1] += 1
        if answers[i] == third[i % 10]:
            score[2] += 1
    for index, value in enumerate(score): #enumerate 리스트의 순서와 값을 반환하는 함수
        if value == max(score):
            answer.append(index+1)
    print(answer)
    return answer
    

answers = [1,3,2,4,2]

solution(answers)