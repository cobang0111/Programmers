def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    
    # Function BFS
    def bfs():
        queue = []
        queue.append((begin, 0))
        while queue:
            cur, time = queue.pop(0)
            for index, word in enumerate(words):
                # Case : Already visit
                if visited[index]:
                    continue
                # Searching that different spell
                possible = True
                count = 0
                for n in range(len(cur)):
                    if cur[n] != word[n]:
                        count += 1
                    if count > 1:
                        possible = False
                        break
                if possible:
                    # Case : Done
                    if word == target:
                        result = time+1
                        return result
                    else:
                        visited[index] = 1
                        queue.append((word, time+1))
        # Impossible return        
        result = 0
        return result
    
    answer = bfs()
    return answer
