# 이코테

n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

'''
a2 = [(i,0) for i in a]
b2 = [(i,1) for i in b]

fin = a2 + b2
fin = sorted(fin, key = lambda x: x[0], reverse=True)

total = 0
k_count = 0
total_count = 0

for val, idx in fin:

    if total_count == n:
        break

    if idx == 0:
        total_count += 1
        total += val

    elif idx == 1 and k_count < k:
        k_count += 1
        total_count += 1
        total += val

    else:
        pass

print(total)
'''

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))