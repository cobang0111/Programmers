def solution(skill, skill_trees):
    answer = 0
    # Simplify skill_trees
    for case in skill_trees:
        string = ''
        for i in case:
            if i in skill:
                string += i
        # Case : Any skill didn't including given skill set 
        if string == '':
            answer += 1
        # Case : All of skill including given skill set and sequential
        elif len(skill) == len(string) and skill == string:
            answer += 1
        # Case : Some of skill including given skill set and sequential 
        elif len(skill) != len(string) and skill[:len(string)] == string:
            answer += 1

    return answer
