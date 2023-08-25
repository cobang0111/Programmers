def solution(n,a,b):
    answer = 0
    A = a-1
    B = b-1
    
    while True:
        A = A//2
        B = B//2
        answer += 1
        if A == B:
            break

    return answer
