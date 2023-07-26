def solution(sizes):
    answer = 0
    max_height = 0
    max_width = 0
    # Sort each business card by size
    for i in sizes:
        i.sort()
        # Get maximum width and height
        if i[0] > max_height :
            max_height = i[0]
        if i[1] > max_width : 
            max_width = i[1]
    # Area
    answer = max_height * max_width
    return answer
