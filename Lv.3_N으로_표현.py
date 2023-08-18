def solution(N, number):
    answer = 0
    
    cycle = 1 #Variable for number of N
    # Initial list
    number_list = [N]
    record = [(cycle, [N])]
    
    # Loop for find all possible number
    while True:
        # End condition
        if number in record[cycle-1][1]:
            break
        if cycle > 8:
            break
            
        new = []
        # Make N, NN, NNN, NNNN ... for each cycle
        i = 0
        num = 0
        while i <= cycle :
            num += N*(10**i)
            i += 1
        new.append(num)
        
        # Make all possible number using DP
        ptr1 = 0
        ptr2 = len(record) - 1
        # number of N in ptr1 + number of N in ptr2 = cycle 
        while True:
            for num_1 in record[ptr1][1]:
                for num_2 in record[ptr2][1]:
                    # + 
                    num_plus = num_2 + num_1 
                    new.append(num_plus)
                    # - 
                    num_minus = abs(num_2 - num_1)
                    new.append(num_minus)
                    # * 
                    num_multiply = num_2 * num_1
                    new.append(num_multiply)
                    # / 
                    if num_1 != 0:
                        num_divide = round(num_2 / num_1)
                        new.append(num_divide)
            ptr1+=1 
            ptr2-=1
            # End condition
            if ptr1 >= ptr2 :
                break
                
        cycle += 1
        # delete duplication
        new = list(set(new))
        record.append((cycle, new))
        number_list.extend(new)
    
    # result    
    if cycle > 8:
        answer = -1
    else:
        answer = cycle
    return answer
