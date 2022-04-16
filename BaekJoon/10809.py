text = input()

for i in range(ord('a'),ord('z')+1):
    if chr(i) in text:
        print(text.index(chr(i)), end=' ')
    
    else:
        print(-1, end=' ')