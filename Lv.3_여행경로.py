
def solution(tickets):
    answer = 0
    tickets.sort()
    path_list = []
    n = len(tickets)
    
    # Function DFS
    def dfs(dprt_airport, path, remain_ticket):
        # Case : Possible
        if len(path) == n+1:
            path_list.append(path)
            return
        # Check tickets
        for tkt in remain_ticket:
            # Case : ticket is non-used and departure airport is collect
            if tkt[0] == path[-1]:
                # Save used_ticket and path before recursion
                temp_remain_ticket = [t for t in remain_ticket]
                temp_path = [p for p in path]
                temp_remain_ticket.remove(tkt)
                temp_path.append(tkt[1])
                dfs(tkt[1], temp_path, temp_remain_ticket)
                # Load saved info
                temp_remain_ticket = remain_ticket
                temp_path = path
        return
    
    dfs("ICN", ["ICN"], tickets)
    #print(path_list)
    path_list.sort()
    
    answer = path_list[0]
    return answer
