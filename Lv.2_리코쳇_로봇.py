def solution(board):
    answer = 0
    
    row = len(board)
    col = len(board[0])
    
    start_row, start_col, exit_row, exit_col = 0, 0, 0, 0
    visited = [[0] * col for i in range(row)]
    
    # Find start and exit point
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                start_row, start_col = i, j
            elif board[i][j] == 'G':
                exit_row, exit_col = i, j
    
    # Function BFS
    def bfs():
        # Start point
        visited[start_row][start_col] = 1
        queue = []
        queue.append((start_row, start_col, 0))
        
        while queue:
            cur_row, cur_col, time = queue.pop(0)
            # Case : Find exit
            if cur_row == exit_row and cur_col == exit_col:
                return time
            # 4 Way (Up, Right, Down, Left)
            for d_row, d_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                temp_row, temp_col = cur_row, cur_col
                # Sliding
                while True:
                    if temp_row + d_row < 0 or temp_row + d_row > row-1 :
                        break
                    if temp_col + d_col < 0 or temp_col + d_col > col-1 :
                        break
                    if board[temp_row + d_row][temp_col + d_col] == 'D':
                        break
                    temp_row += d_row
                    temp_col += d_col
                # Case : non-visited
                if visited[temp_row][temp_col] == 0:
                    visited[temp_row][temp_col] = 1
                    queue.append((temp_row, temp_col, time+1))
        return -1
                   
    answer = bfs()
    
    print(answer)
    
    return answer
