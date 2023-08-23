def solution(n):
    answer = 0
    
    # iterative fibonacci
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append((fibo[i-1] + fibo[i-2]) % 1234567)
    
    answer = fibo[-1]
    
    return answer
