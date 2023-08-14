from itertools import product as p

def solution(word):
    answer = 0
    
    # Make all case and ordered by lexicographic order
    spell_list = ['A', 'E', 'I', 'O', 'U']
    all_case = []
    for i in range(1,6):
        all_case += list(p(spell_list, repeat = i))
    all_case.sort()
    
    # Find word index
    temp = []
    for s in word:
        temp.append(s)
    answer = all_case.index(tuple(temp)) + 1 

    return answer
