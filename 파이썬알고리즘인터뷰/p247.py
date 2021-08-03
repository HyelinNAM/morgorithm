# 중복문자제거 - 중복된 문자를 제외하고 사전식 순서로 나열
import collections

def remove_n_sort(string):

    counter, seen, stack = collections.Counter(string), set(), []

    for s in string:
        counter[s] -= 1

        if s in seen:
            continue

        while stack and s < stack[-1] and counter[stack[-1]] > 0 : # and
            seen.remove(stack.pop())

        stack.append(s)
        seen.add(s)

    return ''.join(stack)

s = 'cbacdcbc'
remove_n_sort(s)
