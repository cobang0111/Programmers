def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i == ")":
            while True:
                if len(stack) == 0:
                    return False
                if stack.pop() == "(":
                    break
        else:
            stack.append(i)
        #print(stack)

    if len(stack) == 0:
        return True
    else:
        return False
