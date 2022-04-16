from itertools import combinations

def solution(nums):
    
    combis = list(combinations(nums,3))
    combis = [c for c in combis if is_prime(sum(c)) == 2]
    
    return len(combis)

def is_prime(n):
    return len([i for i in range(1,n+1) if n%i==0])
