def solution(number, k):
    answer = ''
    
    # Make string number to list
    num_list = []
    for s in number:
        num_list.append(s)
    
    stack = []
    remain = k
    # linear search
    for s in number:
        # Case : Empty stack or remain delete digit = 0
        if remain == 0 or stack == []:
            stack.append(s)
        # Case : Find larger number than the last element of stack
        elif stack[-1] < s:
            while stack and stack[-1] < s and remain > 0:
                stack.pop()
                remain -= 1
            stack.append(s)
        else:
            stack.append(s)
    
    # Case : remain left
    if remain > 0:
        for i in range(remain):
            stack.pop()
    answer = "".join(stack)
    
    return answer
