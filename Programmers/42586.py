import math

def solution(progresses, speeds):
    
    stack = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    stack.reverse()
    
    answer = []
    count = 1
    maximum = stack.pop()
    
    while stack:
        top = stack.pop()
        
        if top > maximum:
            maximum = top
            answer.append(count)
            count = 1
            
        else:
            count += 1 

    answer.append(count)
            
    return answer