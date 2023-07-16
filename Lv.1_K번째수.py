def solution(array, commands):
    answer = []
    for com in commands:
        target = array[com[0]-1:com[1]]
        target.sort()
        answer.append(target[com[2]-1])
    return answer
