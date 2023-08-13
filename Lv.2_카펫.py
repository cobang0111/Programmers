def solution(brown, yellow):
    answer = []
    #brown = 2(a+b) - 4
    #yellow = (a-2) * (b-2)
    
    answer_w = 0
    answer_h = 0
    
    for i in range(1, yellow+1):
        # Find possible a and b
        if yellow % i == 0:
            if i < yellow:
                a = i + 2
                b = yellow // i + 2
            else:
                a = i + 2
                b = i // yellow + 2
            
            # Case : a and b satisfy system of equations
            if (a-2) * (b-2) == yellow and 2*(a + b) - 4 == brown:
                answer_w = a
                answer_h = b
                break
                
    answer = [answer_w, answer_h]
    # width >= height
    answer.sort(reverse = True)
    return answer
