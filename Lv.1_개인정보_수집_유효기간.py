def solution(today, terms, privacies):
    answer = []
    
    #Today
    today_year = int(today[0:4])
    today_month = int(today[5:7]) 
    today_day = int(today[8:10])
    today_int = today_year*10000 + today_month*100 + today_day
    
    #Get All Info using for loop
    for i in range(len(privacies)):
        type = privacies[i][-1]
        valid_month = 0
        #Find type of term
        for j in range(len(terms)):
            if terms[j][0] == type:
                valid_month = int(terms[j][2:])
                break
                
        #Agree Date        
        agree_year = int(privacies[i][0:4])
        agree_month = int(privacies[i][5:7]) 
        agree_day = int(privacies[i][8:10])
        
        #Manufacturing the data to use comfortable
        if agree_day == 1:
            if agree_month == 1:
                agree_year -= 1
                agree_month = 12
                agree_day = 28
            else :
                agree_month -= 1
                agree_day = 28
        else : 
            agree_day -= 1
        
        agree_month += valid_month
        #Case : Added Month > 12
        while(agree_month > 12):
            agree_month -= 12
            agree_year += 1

        #Expire Date    
        valid_int = agree_year*10000 + agree_month*100 + agree_day
        #Case : Expire
        if today_int > valid_int:
            answer.append(i+1)
            
    return answer

