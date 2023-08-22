def solution(n, m, x, y, r, c, k):
    answer = ''
    
    # Initial Setting
    start_x = x-1
    start_y = y-1
    end_x = r-1
    end_y = c-1
    dx = end_x - start_x
    dy = end_y - start_y
    cur_x = start_x
    cur_y = start_y
    
    if (k-(abs(dx) + abs(dy))) % 2 == 1 or abs(dx) + abs(dy) - k > 0:
        answer = "impossible"
    else:
        while len(answer) < k:
            gap = abs(dx) + abs(dy)
            remain = k - len(answer)
            # Case : Remain a lot
            if remain - 2 >= gap :
                if cur_x+1 < n :
                    answer += 'd'
                    cur_x += 1
                    dx -= 1
                elif cur_y-1 >= 0 :
                    answer += 'l'
                    cur_y -= 1
                    dy += 1
                elif cur_y+1 < m :
                    answer += 'r'
                    cur_y += 1
                    dy -= 1
                elif cur_x-1 >= 0  :
                    answer += 'u'
                    cur_x -= 1
                    dx += 1
            # Remain == GAP
            else:
                if dx > 0 :
                    answer += 'd'
                    cur_x += 1
                    dx -= 1
                elif dy < 0 :
                    answer += 'l'
                    cur_y -= 1
                    dy += 1
                elif dy > 0 :
                    answer += 'r'
                    cur_y += 1
                    dy -= 1
                elif dx < 0 :
                    answer += 'u'
                    cur_x -= 1
                    dx += 1      
    return answer
    
    
    
