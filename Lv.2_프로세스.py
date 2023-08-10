def solution(priorities, location):
    answer = 0
    n = len(priorities)
    # priorities with index
    index_p = [(i, priorities[i]) for i in range(n)]
    
    conduct_list = []
    # Loop: Until doing all of task
    while priorities:
        # Sort by priority
        priorities.sort(reverse = True)
        # Bring target from queue
        target = index_p.pop(0)
        # Case : Target is the most priority
        if target[1] >= priorities[0]:
            conduct_list.append(target[0])
            priorities.pop(0)
        # Case : Target is NOT the most priority
        else:
            index_p.append(target)
    
    answer = conduct_list.index(location) + 1
    
    return answer
