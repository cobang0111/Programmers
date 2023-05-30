#https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    #Make Score Board
    score = [['R',0],['T',0],['C',0],['F',0],['J',0],['M',0],['A',0],['N',0]]
    #Analysis Survey
    for i in range(len(survey)):
        #Case : choices < 4 => Add to prefix
        if choices[i] < 4:
            #Add on score board
            for k in score: 
                if k[0] == survey[i][0]:
                    k[1] += 4 - choices[i]
                    break
        #Case : choices > 4 => Add to postfix
        elif choices[i] > 4:
            #Add on score board
            for k in score: 
                if k[0] == survey[i][1]:    
                    k[1] += choices[i] - 4
                    break
    #Analysis score board            
    for i in range(0, len(score), 2):
        #Case : prefix > postfix
        if score[i][1] > score[i+1][1]:
            answer += score[i][0]
        #Case : prefix < postfix
        elif score[i][1] < score[i+1][1]:
            answer += score[i+1][0]
        #Case : prefix = postfix -> lexicographical order
        elif ord(score[i][0]) < ord(score[i+1][0]):
            answer += score[i][0]
        else:
            answer += score[i+1][0]
    return answer
