from itertools import product
def solution(n, info):
    answer = []
    max_diff = 0
    max_lion_score = 0
    cur_appeach_score = 0
    
    #Naive 2^11 case using product
    for case in product((True, False), repeat=11):
        lion_score = 0
        appeach_score = 0
        cost = 0
        
        # Calculate scores for each case
        for i in range(len(case)):
            if case[i] == True:
                lion_score += 10-i
                cost += info[i]+1
            elif case[i] == False and info[i] != 0:
                appeach_score += 10-i
        
        diff = lion_score - appeach_score
        
        #Update case
        if cost <= n and diff > 0 and diff >= max_diff:
            #Make the result list
            result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(case)):
                if case[i] == True:
                    result[i] = info[i]+1
            #Remain cost added to 0 point
            result[10] += n - cost
            #Case : diff is same -> decide the case that recieve more lower point
            if diff == max_diff and result != answer :
                #Comparing
                for i in range(len(case)-1,-1,-1):
                    if answer[i] < result[i]:
                        answer = result
                        break
                    elif answer[i] > result[i]:
                        break
            #Case : New case has more larger difference
            elif diff > max_diff :
                max_diff = diff
                answer = result

    #No case or draw case
    if answer == [] or answer == info:
        answer = [-1]
    
    return answer
