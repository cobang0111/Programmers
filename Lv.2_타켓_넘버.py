def solution(numbers, target):
    
    def dfs(index, result):
        nonlocal answer
        #end of depth
        if index == len(numbers):
            if result == target:
                answer += 1
            return
        #dfs recursive part
        dfs(index + 1, result + numbers[index])
        dfs(index + 1, result - numbers[index])
    
    answer = 0
    dfs(0, 0)
    return answer
