#  괄호
n = int(input())

def check_bracket(text):

    stack = []

    for t in text:
        if t == '(':
            stack.append(t)
        else:
            if stack: # not empty
                stack.pop()
            else:
                return 'NO'

    if stack:
        return 'NO'
    else:
        return 'YES'

for _ in range(n):
    print(check_bracket(input()))