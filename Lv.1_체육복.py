def solution(n, lost, reserve):
    # Initial setting (Students who lost but have extra suit)
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    new_lost.sort()
    count = 0
    # Find gymsuit from i-1 and i+1 student
    for i in new_lost:
        if i != 1 and (i-1) in new_reserve:
            new_reserve.remove(i-1)
            count+=1
        elif i != n and (i+1) in new_reserve:
            new_reserve.remove(i+1)
            count+=1
    answer = n - len(new_lost) + count
    return answer
