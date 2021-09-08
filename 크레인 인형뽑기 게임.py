# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:08:15 2021

@author: kim
"""

def solution(board, moves):
    bucket = [0]
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                if bucket[-2] == bucket[-1]:
                    bucket.pop(-1)
                    bucket.pop(-1)
                    answer = answer + 1
                board[i][move-1] = 0
                break
    return answer*2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
