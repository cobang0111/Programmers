def solution(m, n, puddles):
    answer = 0
    
    given_map = [[0] * m for _ in range(n)]
    for j,i in puddles:
        given_map[i-1][j-1] = -1
        
    # First row
    for j in range(m):
        if given_map[0][j] == -1:
            break
        else :
            given_map[0][j] = 1
    # First column
    for i in range(n):
        if given_map[i][0] == -1:
            break
        else :
            given_map[i][0] = 1
    
    # Remain
    for i in range(1, n):
        for j in range(1, m):
            if given_map[i][j] == -1:
                continue
            elif given_map[i-1][j] == -1 and given_map[i][j-1] == -1:
                given_map[i][j] = 0
            elif given_map[i-1][j] == -1:
                given_map[i][j] = given_map[i][j-1]
            elif given_map[i][j-1] == -1:   
                given_map[i][j] = given_map[i-1][j]
            else:
                given_map[i][j] = given_map[i-1][j] + given_map[i][j-1]
    
    #print(given_map)
    answer = given_map[n-1][m-1] % 1000000007
    
    return answer
