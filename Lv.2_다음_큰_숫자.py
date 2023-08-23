def solution(n):
    answer = 0
    
    # count 1 in n
    target = 0
    for i in str(bin(n))[2:]:
        if i == '1':
            target+=1
    print(target)
    
    # Find next n
    next_n = n
    while True:
        next_n += 1
        count = 0
        # Count 1 in current n
        for s in str(bin(next_n))[2:]:
            if s == '1':
                count += 1
            if count > target:
                break
        # Case : Find
        if count == target:
            break
    answer = next_n
    return answer
