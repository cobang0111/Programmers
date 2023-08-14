from itertools import permutations as p

def solution(k, dungeons):
    answer = -1
    
    # Brute - Force
    for i in range(len(dungeons), 0, -1):
        # Make permutation
        for case in list(p(dungeons, i)):
            temp_k = k
            success = True
            # Possibility
            for need, use in case:
                if temp_k < need:
                    success = False
                    break
                else:
                    temp_k -= use
            if success:
                answer=len(case)
                return answer
    
    answer = 0
    return 0
