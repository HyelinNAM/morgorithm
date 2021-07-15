# 애너그램
from collections import defaultdict

def anagram(input):
    result = defaultdict(list)

    for i in input:
        k = "".join(sorted(i))
        result[k].append(i)

    return result.values()


input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagram(input)