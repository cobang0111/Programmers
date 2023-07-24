def solution(n, edge):
    answer = 0
    
    # Function : BFS
    def bfs(vertex):
        # Starting vertex
        visited[vertex-1] = True
        min_dist[vertex-1] = 0
        q.append(vertex) #Queue
        # Loop for BFS
        while len(q) > 0 :
            new_vertex = q.pop(0)
            # BFS using adjacency list
            for next_vertex in adj_list[new_vertex-1]:
                if visited[next_vertex-1] == False:
                    q.append(next_vertex)
                    visited[next_vertex-1] = True
                    # Case : Update minimum distance list
                    if min_dist[new_vertex-1] + 1 < min_dist[next_vertex-1]:
                        min_dist[next_vertex-1] = min_dist[new_vertex-1] + 1 
    
    #Initial Setting
    visited = [False for _ in range(n)]
    q = []
    adj_list = []
    for i in range(n):
        adj_list.append([])
    min_dist = [999999 for _ in range(n)]    
    #Make adjacency list
    for e in edge:
        adj_list[e[0]-1].append(e[1])
        adj_list[e[1]-1].append(e[0])
    
    # BFS always starting from vertex 1
    bfs(1)
    # Count the number of fallest node
    maximum = max(min_dist)
    for i in min_dist:
        if i == maximum:
            answer += 1
    
    return answer
