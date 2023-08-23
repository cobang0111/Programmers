def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        temp_sum = 0
        while temp_sum < n:
            temp_sum += i
            if temp_sum == n:
                answer += 1
            i+=1
    
    return answer
