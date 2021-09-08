# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:19:52 2021

@author: kim
"""
import re

def solution(new_id):
    answer = ''
    useword_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                    'o','p','q','r','s','t','u','v','w','x','y','z','-','_','.',
                    '0','1','2','3','4','5','6','7','8','9']
    #1단계
    new_id = new_id.lower()
    
    #2단계
    for char in new_id:
        if char in useword_list:
            answer = answer + char

    #3단계
    answer = re.sub('(([.])\\2{1,})', '.', answer)
    
    #4단계
    while(True):
        if  len(answer) != 0 and answer[0] == '.':
            answer = answer[1:]
        elif len(answer) != 0 and answer[-1] == '.':
            answer = answer[:-1]
        else:
            break

    #5단계
    if len(answer) == 0:
        answer = answer + 'a'
        
    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7단계
    while(len(answer) <= 2):
        answer = answer + answer[-1:]

    return answer

new_id = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p" ]

for id in new_id:
    print(solution(id))
