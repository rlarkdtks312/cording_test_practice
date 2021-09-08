# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:33:01 2021

@author: kim
"""

def solution(numbers, hand):
    answer = ''
    left_location = [0,3]
    right_location = [2,3]
    l = [1,4,7, '*']
    r = [3, 6, 9, '#']
    number_location = [[0,0],[1,0],[2,0],
                       [0,1],[1,1],[2,1],
                       [0,2],[1,2],[2,2],
                       [0,3],[1,3],[2,3]]

    
    for i in range(len(numbers)):
        position = 10 if numbers[i] == 0 else numbers[i]-1
        if numbers[i] in l:
            answer = answer + 'L'
            left_location = number_location[position]
        elif numbers[i] in r:
            answer = answer + 'R'
            right_location = number_location[position]
        else:
            if abs(left_location[0]-number_location[position][0]) + abs(left_location[1]-number_location[position][1]) == \
            abs(right_location[0]-number_location[position][0]) + abs(right_location[1]-number_location[position][1]):
                print('same')
                if hand == 'left':
                    answer = answer + 'L'
                    left_location = number_location[position]
                elif hand == 'right':
                    answer = answer + 'R'
                    right_location = number_location[position]
            elif abs(left_location[0]-number_location[position][0]) + abs(left_location[1]-number_location[position][1]) > \
            abs(right_location[0]-number_location[position][0]) + abs(right_location[1]-number_location[position][1]):
                answer = answer + 'R'
                right_location = number_location[position]
            else:
                answer = answer + 'L'
                left_location = number_location[position]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right' #'right'

answer = solution(numbers, hand)
print(answer)
