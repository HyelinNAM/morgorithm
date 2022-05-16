def solution(clothes):
    
    clothes_dict = {}
    
    for name, kind in clothes:
        if clothes_dict.get(kind):
            clothes_dict[kind] += 1
            
        else:
            clothes_dict[kind] = 1
    
    # answer = 1
    # for c in clothes_dict.values():
    #     answer *= (c+1)

    from functools import reduce
    answer = reduce(lambda x,y: x*(y+1), clothes_dict.values(), 1)
    
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))