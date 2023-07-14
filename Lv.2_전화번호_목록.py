def solution(phone_book):
    answer = True
    #Make length list
    length_list = []
    for i in phone_book:
        if len(i) not in length_list:
            length_list.append(len(i))

    #Make hash of phone 
    #Finding target in hash take O(1)
    hash_phone = {}
    for number in phone_book:
        hash_phone[hash(number)] = number 
    
    for j in length_list:
        for number in phone_book:
            #Case prefix
            if j < len(number):
                #Case target in hash
                if hash(number[:j]) in hash_phone:
                    answer = False
                    return answer
                
    return answer
