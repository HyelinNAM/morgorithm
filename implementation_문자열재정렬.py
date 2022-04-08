string = input()

alpha = []
num = 0

for s in string:
    if s.isalpha():
        alpha.append(s)
    
    else:
        num += int(s)

alpha = sorted(alpha)

if num > 0:
    alpha.ppend(str(num))
    
print(''.join(alpha))