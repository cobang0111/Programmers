def solution(s):
    answer = ''
    s = s.lower()
    L = list(s)
    
    for i in range(len(L)):
        if i == 0 and L[i].islower():
            L[i] = L[i].upper()
        elif L[i-1] == ' ':
            L[i] = L[i].upper()
    
    answer = ''.join(L)
    return answer
