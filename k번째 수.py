# -*- coding: utf-8 -*-
def solution(array, commands):
    answer = []
    for i in commands:
        j = i[0]-1
        q = i[1]
        k = i[2]-1
        temp = sorted(array[j:q])
        answer.append(temp[k])
    return answer
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
answer = solution(array, commands)

print(answer)