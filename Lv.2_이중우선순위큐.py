def solution(operations):
    queue = []
    
    for string in operations:
        # Data slicing
        string_list = string.split() 
        order = string_list[0]
        num = int(string_list[1])
        # Case : Insert
        if order == "I":
            queue.append(num)
        # Case : Delelte max from non-empty queue
        elif num == 1 and queue:
            queue.pop()
        # Case : Delelte min from non-empty queue
        elif num == -1 and queue:
            queue.pop(0)
        else:
            continue
        queue.sort()
    
    if queue:
        answer = [queue[-1], queue[0]]
    else:
        answer = [0, 0]
    return answer
