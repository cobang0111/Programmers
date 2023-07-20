import heapq

def solution(jobs):
    #Make jobs to heap (ordered by ASC request time)
    heapq.heapify(jobs)
    #Initial setting
    n = len(jobs)
    in_task = [] #Processing task
    wait_task = [] #Waiting task heap
    time = 0
    total = 0
    count = 0
    pop_time = -1

    while count < n:
        # Case : There is no processing task
        if len(in_task) == 0:
            task = heapq.heappop(jobs)
            in_task.append(task)
            time = task[0]
            pop_time = task[0] + task[1]
            total += task[1]
        # Case : Time to processing remain request but there is processing task
        elif jobs and time == jobs[0][0]:
            request, take = heapq.heappop(jobs)
            # push to waiting heap (ordered by ASC taking time)
            heapq.heappush(wait_task, (take, request))
        # Case : Time to end processing
        elif time == pop_time:
            in_task.pop()
            count += 1
            # Case : Waiting task exist -> pop from waiting heap
            if wait_task:
                take, request = heapq.heappop(wait_task)
                task = [request, take]
                in_task.append(task)
                pop_time = time + task[1]
                total += pop_time - task[0]
        else :
            time += 1

    answer = total // n
    return answer
