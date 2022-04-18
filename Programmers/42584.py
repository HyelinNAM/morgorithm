# 주식 가격

def solution(prices):
    
    prices = [(p,i) for i,p in enumerate(prices)]
    stack = []
    answer = [0] * len(prices) # stack
    
    for p in prices:
        while stack and (stack[-1][0] > p[0]):
                pop = stack.pop()
                answer[pop[1]] = p[1] - pop[1]
        stack.append(p)
    
    while stack:
        pop = stack.pop()
        answer[pop[1]] = p[1] - pop[1]
            
    return answer