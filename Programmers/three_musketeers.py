#프로그래머스(삼총사)
from itertools import combinations
def solution(number):
    answer = 0
    three = list(combinations(number,3))
    for i in range(len(three)):
        if(sum(three[i])==0):
            answer += 1
    return answer
