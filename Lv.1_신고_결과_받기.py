#https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    #Make initial answer list
    for i in range(len(id_list)):
        answer.append(0)
    #Make initial report info list
    report_list = [[i, 0, []] for i in id_list]
    
    #Update report info to report_list
    for i in report:
        temp_L = i.split()
        report_index = id_list.index(temp_L[0])
        reported_index = id_list.index(temp_L[1])
        #Append reported user and times without duplication
        if temp_L[1] not in report_list[report_index][2]:
            report_list[report_index][2].append(temp_L[1])
            report_list[reported_index][1] += 1           
    
    #Make ben user list
    ben_user = []
    for i in report_list:
        if i[1] >= k:
            ben_user.append(i[0])
            
    #Find user who report ben user
    for i in range(len(report_list)):
        for j in ben_user:
            if j in report_list[i][2]:
                answer[i]+=1
                           
    return answer
