def solution(n):
    answer = []
    
    # Recursive hanoi function
    def hanoi(n, start, end):
        # Determine the stick that isn't both start and end
        temp = [1, 2, 3]
        temp.remove(start)
        temp.remove(end)
        remain = temp.pop()
        # Recursive 
        if n > 1:
            hanoi(n-1, start, remain)
            answer.append([start, end])
            hanoi(n-1, remain, end)
        # n = 1
        else:
            answer.append([start, end])
        
    hanoi(n, 1, 3)
    
    return answer
