def solution(numbers):
    answer = []
    
    # Make Decimal N to binary N 
    # Binary N have full binary tree length
    bin_num = []
    
    for num in numbers:
        cur = str(bin(num))[2:]
        height = 0
        while True:
            if pow(2,height) - 1< len(cur):
                height += 1
            else :
                break
        add = pow(2,height) - 1 - len(cur)
        for i in range(add):
            cur = '0' + cur
        bin_num.append(cur)
    
    # Possibility
    boole = True
    # Function : Recursion tree searching 
    def slicing(string):
        nonlocal boole
        #Leaf Node -> No mattor 0 or 1
        if len(string) == 1:
            return
        mid = len(string) // 2 # Root of each subtree
        # Case : Root of subtree is 0
        if string[mid] == '0':
            for i in range(len(string)):
                # when Root is 0 -> all sub tree be 0
                if string[i] != '0':
                    boole = False
                    return
        # Recursion
        slicing(string[0:mid])
        slicing(string[mid+1:])
    # Make Answer
    for x in bin_num:
        slicing(x)
        if boole == False:
            answer.append(0)
        else:
            answer.append(1)
        boole = True
    return answer
