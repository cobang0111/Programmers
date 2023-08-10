def solution(n, computers):
    answer = 0
    
    # Function : DFS (adjacency matrix)
    visited = [False for _ in range(n)]
    def dfs(vertex):
        visited[vertex] = True
        for i in range(n):
            if i != vertex and computers[vertex][i] == 1 and visited[i] == False:
                dfs(i)
    
    # Separating group using dfs
    all_visited_list = []
    for x in range(n):
        visited = [False for _ in range(n)]
        dfs(x)
        visited_list = []
        for y in range(len(visited)):
            if visited[y]:
                visited_list.append(y)
        visited_list.sort()
        if visited_list not in all_visited_list:
            all_visited_list.append(visited_list)
    
    answer = len(all_visited_list)
            
    return answer
