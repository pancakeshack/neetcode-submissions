class Solution:
    def isValid(self, s: str) -> bool:
        closers = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for c in s:
            if c in closers:
                stack.append(c)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if c != closers[temp]:
                    return False

        if len(stack) != 0:
            return False
        
        return True