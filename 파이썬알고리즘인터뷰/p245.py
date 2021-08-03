# 괄호로 입력된 값이 올바른지 판별
 
# 여는 괄호 / 닫는 괄호 구분. 여는 괄호는 스택으로. 닫는 괄호 나오면 pop 하면서 pair 체크
def is_valid(string):

    stack = []
    pair = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for s in string:
        if s not in pair: # 여는 괄호 - (, {, [
            stack.append(s) # = push

        elif not stack or pair[s] != stack.pop():
            return False
        
    return len(stack) == 0


s = "(){[]}"
is_valid(s)
