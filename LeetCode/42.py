# Trapping Rain Water - △△△

class Solution:
    def trap(self, height: List[int]) -> int:
    
        stack = [height[0]]
        max = height[0]
        volume = 0

        for h in height[1:]:

            stack.append(h)

            if h >= max:
                for t in stack[1:-1]: # 1:-1
                    volume += max-t

                max = h
                stack = [h] # stack.append(h)

        if stack: # stack이 차있다면
            height = stack.copy()
            height.reverse()

            stack=[height[0]]
            max = height[0]

            for h in height[1:]:

                stack.append(h)

                if h >= max:
                    for t in stack[1:-1]:
                        volume += max-t

                    max = h
                    stack = [h]

        return volume