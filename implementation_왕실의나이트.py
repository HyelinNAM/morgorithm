loc = input()
loc = (ord(loc[0]), int(loc[1]))

move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count = 0
for m in move:
    dx = loc[0] + m[0]
    dy = loc[1] + m[1]

    if ord('a') > dx or ord('h') < dx or dy < 1 or dy > 8:
        continue
    else:
        count +=1

print(count)
