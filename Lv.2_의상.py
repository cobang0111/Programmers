def solution(clothes):
    
    dic_clothes = {}    
    
    # Make Dictionary
    for name, typ in clothes:
        if typ in dic_clothes:
            dic_clothes[typ].append(name)
        else:
            dic_clothes[typ] = [name]
    
    # Possible case = total product of
    # Number of clothes for each type + 1 (no wearing case ~ number of wears)
    answer = 1
    for key in dic_clothes:
        answer *= len(dic_clothes.get(key)) + 1
    # But non-wearing all of clothes is impossible
    answer -= 1
    return answer
