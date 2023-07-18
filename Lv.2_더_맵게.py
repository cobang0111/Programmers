import heapq

def solution(scoville, K):
    answer = 0
    # Make Heap
    heapq.heapify(scoville)
    # Loop for Mixing
    while scoville[0] < K:
        # Case : Impossible
        if len(scoville) < 2 or scoville[0] == 0 or scoville[1] == 0:
            return -1 
        # Pop 2 mininmum element from heap
        least = heapq.heappop(scoville)
        next_least = heapq.heappop(scoville)
        # Push mix element to heap
        heapq.heappush(scoville, least+2*next_least)
        answer += 1
    return answer
