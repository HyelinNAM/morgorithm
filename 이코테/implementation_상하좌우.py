space = int(input())
move = input().split() # > list

x = 1 
y = 1

info = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

for m in move:

    dx = x + info[m][0]
    dy = y + info[m][1]

    if dx < 1 or dx > space or dy < 1 or dy > space:
        continue

    x = dx
    y = dy

print(x,y)
