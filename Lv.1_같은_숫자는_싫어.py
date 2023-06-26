def solution(arr):
    
    answer = [] 
    con = [] #Consecutive judging stack
    
    for i in range(len(arr)):
        #initial element
        if i==0:
            con.append(arr[i])
            answer.append(arr[i])
        else :
            #Case : Not consecutive -> push to stack 
            if con[0] != arr[i]:
                con.pop()
                con.append(arr[i])
                answer.append(arr[i])
                
    return answer
