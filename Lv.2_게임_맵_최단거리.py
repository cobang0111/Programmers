#Solve by dijkstra and heap
#Not DFS/BFS
import heapq
global INF
INF = 99999

def dijkstra(start, map):
    row = len(map)
    col = len(map[0])
    dist = [[INF] * col for _ in range(row)]
    dist[start[0]][start[1]] = 0
    heap = [(0, start)]
    #Fill the dist map with minimum cost to reach to the each box
    while heap:
        cost, pos = heapq.heappop(heap)
        if dist[pos[0]][pos[1]] < cost:
            continue
        # 4 Way
        for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_row, next_col = pos[0] + delta_row, pos[1] + delta_col
            # Case : Index out of range
            if next_row < 0 or next_col < 0 or next_row >= row or next_col >= col:
                continue
            # Case : Wall
            if map[next_row][next_col] == 0:
                continue
            # Update when the cost is smaller than previous one.
            next_cost = cost + 1
            if next_cost < dist[next_row][next_col]:
                dist[next_row][next_col] = next_cost
                heapq.heappush(heap, (next_cost, (next_row, next_col)))
                
    return dist[row-1][col-1]

def solution(maps):
    answer = 0
    
    result = dijkstra((0, 0), maps)
    # Case : No way
    if result == INF:
        answer = -1
    # Case : Way exist
    else :
        #We have to return the number of box
        answer = result + 1
    
    return answer
