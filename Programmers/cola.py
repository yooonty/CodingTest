#프로그래머스(콜라 문제)
def solution(a, b, n):
    answer = 0
    while (n>=a):
        answer += (n//a)*b
        n = n - (n//a)*a + (n//a)*b
    return answer
