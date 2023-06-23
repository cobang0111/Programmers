import itertools

def solution(users, emoticons):
    answer = [0, 0] #Initial setting
    
    #Make ALL of Price Case using Cartesian Product
    all_price_case = []
    
    #Save each emoticons' saled price and append it to larger list
    for i in emoticons:
        price_case = [] 
        for sale in [0.1, 0.2, 0.3, 0.4]:
            price_case.append(round(i * (1-sale)))   
        all_price_case.append(price_case)
    
    #Cartesian Product of each case (len(emoticons) <= 7)
    #Naive... -> improvement needed
    all_case = []
    if len(emoticons) == 1:
        result = all_price_case[0]
        all_case = list(result)
    elif len(emoticons) == 2:
        result = itertools.product(all_price_case[0], all_price_case[1])
        all_case = list(result)
    elif len(emoticons) == 3:
        result = itertools.product(all_price_case[0], all_price_case[1], all_price_case[2])
        all_case = list(result)
    elif len(emoticons) == 4:
        result = itertools.product(all_price_case[0], all_price_case[1], all_price_case[2], all_price_case[3])
        all_case = list(result)
    elif len(emoticons) == 5:
        result = itertools.product(all_price_case[0], all_price_case[1], all_price_case[2], all_price_case[3], all_price_case[4])
        all_case = list(result)
    elif len(emoticons) == 6:
        result = itertools.product(all_price_case[0], all_price_case[1], all_price_case[2], all_price_case[3], all_price_case[4], all_price_case[5])
        all_case = list(result)
    elif len(emoticons) == 7:
        result = itertools.product(all_price_case[0], all_price_case[1], all_price_case[2], all_price_case[3], all_price_case[4], all_price_case[5], all_price_case[6])
        all_case = list(result)
    
    #Find most efficient sale percent by searching all of price case
    for i in range(len(all_case)):
        count_member = 0
        total_cost = 0
        #Calculate for each user
        for lb_sale, ub_price in users:
            user_total_cost = 0
            #Calculate for each emoticon
            for j in range(len(all_case[i])):
                #Case : Current sale(%) is satisfied lower bound of sale(%)
                if lb_sale <= (emoticons[j]-all_case[i][j])*100/emoticons[j]:
                    user_total_cost += all_case[i][j]
            #Case : Buying subscribe is better
            if user_total_cost >= ub_price:
                count_member += 1
            #Total selling of emoticon without subscribers
            else :
                total_cost += user_total_cost
        #Case : Update (current subscribers are more than before 
        # or subscribers are same but total revenue is larger)
        if count_member > answer[0] or (count_member == answer[0] and total_cost > answer[1]):
                answer[0] = count_member
                answer[1] = total_cost
    
    return answer
