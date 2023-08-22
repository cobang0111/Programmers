def solution(s):
    answer = ''
    
    L = s.split()
    L = list(map(int, L))
    L.sort()
    #print(L)
    
    answer += str(L[0])
    answer += ' '
    answer += str(L[-1])
    
    return answer
