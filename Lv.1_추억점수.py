def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        total = 0
        for j in photo[i]:
            if j in name:
                total += yearning[name.index(j)]
        answer.append(total)
    return answer
