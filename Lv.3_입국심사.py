def solution(n, times):
    answer = 0
    # Set maximum time
    max_time = max(times) * round(n / len(times))
    # Initial Setting
    left = 0
    right = max_time
    # Binary Search
    while (left < right - 1):
        mid = (right + left) // 2   
        # Count the number of persons in given time
        count = 0
        for i in times:
            count += mid // i
        # Left bound case
        if count >= n:
            right = mid
        # Right bound case
        elif count < n:
            left = mid
    # Result
    answer = right
    return answer
