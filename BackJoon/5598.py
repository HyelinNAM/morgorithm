text = list(input())
text = [chr(ord(t) - 3) if ord(t) - 3 >= 65 else chr(ord(t) + 23)  for t in text]

print(''.join(text))
