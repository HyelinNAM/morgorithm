from itertools import permutations

def solution(numbers):
    
    number_list = list(numbers)
    
    candidates = set([int(''.join(c)) for i in range(1, len(numbers)+1) for c in permutations(number_list,i)])
    
    answer = len(candidates)
    
    for c in candidates:
        
        if c <= 1:
            answer -= 1
            pass
        
        for i in range(2,c):
            if c % i == 0:
                answer -= 1
                break
                
    return answer