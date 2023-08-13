
def solution(n, costs):
    answer = 0
    # Sort with the cost by ASC
    costs.sort(key = lambda costs:costs[2])
    
    connected = []
    
    #print(costs)

    count = 0
    #Prim's Algorithm
    while count < n-1:
        for edge in costs:
            # Case : first element
            if connected == []:
                connected.append(edge[0])
                connected.append(edge[1])
                answer += edge[2]
                break
            # Find minimum cost edge that only one element already connected 
            elif edge[0] in connected and edge[1] not in connected:
                connected.append(edge[1])
                answer += edge[2]
                break
            elif edge[0] not in connected and edge[1] in connected:
                connected.append(edge[0])
                answer += edge[2]
                break
        count += 1
    return answer
