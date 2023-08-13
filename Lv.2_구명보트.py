def solution(people, limit):
    # Greedy Approach
    answer = 0
    people.sort()
    cur = 0
    left = 0
    right = len(people) - 1
    # Binary Searching
    while left <= right:
        # Priority to heavy person
        cur = people[right]
        right -= 1
        # Case : If the most light-person in the island ...
        # can take the boat with heavy person
        if cur + people[left] <= limit:
            left += 1
        answer += 1
        
    return answer
