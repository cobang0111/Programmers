def solution(triangle):
    answer = 0
    
    # Line from the bottom
    for i in range(len(triangle)-2, -1, -1):
        # element from the left
        for j in range(len(triangle[i])):
            # Compare below element to find bigger one
            if triangle[i+1][j] >= triangle[i+1][j+1]:
                triangle[i][j] += triangle[i+1][j]
            else:
                triangle[i][j] += triangle[i+1][j+1]
                    
    answer = triangle[0][0]
    
    return answer
