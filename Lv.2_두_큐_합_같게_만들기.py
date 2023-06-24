def solution(queue1, queue2):
    answer = -2
    
    odd = False
    total = float(sum(queue1) + sum(queue2))
    target = total/2 #target sum
    
    #if total is odd -> not separtable equally
    if total%2 != 0:
        odd = True
        
    #Make circular queue and pointer to process fastly 
    #if 1 element pop from queue front, 
    #then it will be pushed to end of another queue
    circular_queue = queue1 + queue2
    queue1_p = 0
    queue2_p = len(queue1)
    
    #Case : Impossible
    if odd or max(circular_queue) > target:
        answer = -1
        return answer
    else :
        count = 0
        cur = float(sum(queue1)) #Current summation value of queue1
        while True:
            #Case : current sum = target sum -> Process determined 
            if cur == target:
                answer = count
                return answer
            #Case : Over the Maximum possible case -> Impossible
            if count >= len(queue1)*4:
                answer = -1
                return answer
            #Case : sum of queue1 > target sum
            if cur > target:
                item = circular_queue[queue1_p]
                queue1_p += 1
                #Case : Pointer index over the length
                if queue1_p >= len(circular_queue):
                    queue1_p -= len(circular_queue)
                cur -= item
                count += 1
            #Case : sum of queue2 > target sum
            else :
                item = circular_queue[queue2_p]
                queue2_p += 1
                #Case : Pointer index over the length
                if queue2_p >= len(circular_queue):
                    queue2_p -= len(circular_queue)
                cur += item
                count += 1
            
        
