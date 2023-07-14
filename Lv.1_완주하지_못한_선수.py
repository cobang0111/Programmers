def solution(participant, completion):
    dict_participant = {}
    sum_key = 0
    
    # Hash for participant
    for i in participant:
        dict_participant[hash(i)] = i
        sum_key += hash(i)
    
    # Find key who didn't complete the race from completion
    for j in completion:
        sum_key -= hash(j)
        
    answer = dict_participant[sum_key]
    return answer
