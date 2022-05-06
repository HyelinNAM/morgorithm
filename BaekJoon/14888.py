n = int(input())
numbers = list(map(int, input().split())) 
operators = list(map(int, input().split())) # +, -, x, //

minimum = 1e+09
maximum = -1e+09

def dfs(depth, cur, ops):
    global minimum, maximum

    if depth == n:
        if cur > maximum:
            maximum = cur

        if cur < minimum:
            minimum = cur
        
        return

    if ops[0] > 0:
        ops[0] -= 1
        dfs(depth+1, cur + numbers[depth], ops)
        ops[0] += 1

    if ops[1] > 0:
        ops[1] -= 1
        dfs(depth+1, cur - numbers[depth], ops)
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        dfs(depth+1, cur * numbers[depth], ops)
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        dfs(depth+1, int(cur / numbers[depth]), ops)
        ops[3] += 1
   
dfs(1, numbers[0], operators)

print(maximum)
print(minimum)
