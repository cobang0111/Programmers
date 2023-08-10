def solution(citations):
    citations.sort(reverse = True)
    max_h = citations[0]
    
    while True:
        if max_h <= len(citations) and citations[max_h-1] >= max_h:
            answer = max_h
            break
        else :
            max_h -= 1
        
    return answer
