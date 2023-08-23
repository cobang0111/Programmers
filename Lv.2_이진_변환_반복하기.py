def solution(s):
    answer = []
    cycle = 0
    remove = 0
    
    while s != "1":
        while '0' in s:
            s=s.replace('0', '', 1)
            remove += 1
        s = str(bin(len(s)))[2:]
        cycle += 1
        
    answer.append(cycle)
    answer.append(remove)
    return answer
