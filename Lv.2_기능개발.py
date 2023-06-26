def solution(progresses, speeds):
    answer = []
    
    temp = progresses
    release = 0
    count = 0
    
    while True:
        #Case : Prefer task done under 100%
        if temp[release] < 100 :
            if count != 0:
                answer.append(count)
                count = 0
            for i in range(len(temp)):
                temp[i] += speeds[i]
        #Case : Prefer task done!
        else:
            count += 1 #Count the task which be released
            release += 1 #Judging next task
            #Case All task be released -> break
            if release == len(progresses):
                answer.append(count)
                break
                
    return answer
