from itertools import permutations

def solution(numbers):
    answer = 0
    
    number_list = [i for i in numbers]
    cases = []
    
    # Find all case
    for n in range(1, len(number_list)+1):
        perm = list(permutations(number_list, n))
        for t in perm:
            result = int(''.join(t))
            if result not in cases:
                cases.append(result)
    
    # Find Prime number
    for num in cases:
        if num > 1:
            # Fundamental Theorem of Arithmetic
            sqrt = round(num**0.5)
            prime = True
            for i in range(2, sqrt+1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                #print(num, sqrt)
                answer+=1
                
    return answer
