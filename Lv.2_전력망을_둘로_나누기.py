def solution(n, wires):
    
    #Initial Setting
    min_diff = n
    
    #dfs function using adjacency list
    def dfs(vertex) :
        nonlocal count
        nonlocal visited
        nonlocal adjacency_list
        visited[vertex-1] = True
        count += 1
        for next_vertex in adjacency_list[vertex-1]:
            if visited[next_vertex-1] == False:
                dfs(next_vertex)
    
    # For all case
    for i in range(n-1):
        # Make new wires list that 1 edge be cutted
        temp_wires = wires[0:i] + wires[i+1:]
        # Initial State
        visited = [False for _ in range(n)]
        count = 0
        adjacency_list = []
        for i in range(n):
            adjacency_list.append([])
        # Make graph using adj list
        for edge in temp_wires:
            adjacency_list[edge[0]-1].append(edge[1])
            adjacency_list[edge[1]-1].append(edge[0])
        # Find connected graph using DFS
        dfs(1)
        diff = abs(count - (n - count))
        # Case : Update
        if diff < min_diff :
            min_diff = diff
    
    answer = min_diff
    return answer
