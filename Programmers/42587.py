# 프린터

def solution(priorities, location):
    
    queue = [[i,p] for i, p in enumerate(priorities)]
    ps = sorted(priorities)
    count = 0
    
    while queue:
        if queue[0][1] != ps[-1]:
            queue.append(queue.pop(0))
        else:
            count += 1
            ps.pop()
            print = queue.pop(0)
            
            if print[0] == location:
                break

    return count