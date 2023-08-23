def solution(n, words):
    # Success stack
    stack = []
    
    for i, word in enumerate(words):
        # Case : First
        if i == 0:
            stack.append(word)
            continue
        # Case : Success
        if stack[-1][-1] == word[0] and word not in stack:
            stack.append(word)
        # Case : Fail -> Find the user and cycle using index who failed 
        else:
            answer = [i % n + 1, i//n + 1]
            break

    if stack == words:
        answer = [0, 0]
    
    return answer
