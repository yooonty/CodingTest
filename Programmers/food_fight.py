#프로그래머스(푸드 파이트 대회)
import math
def solution(food):
    answer = ''
    player = ""
    for i in range(1,len(food)):
        for j in range(0,math.floor(food[i]/2)):
            player += str(i)
    answer = player + "0" + player[::-1]
    return answer