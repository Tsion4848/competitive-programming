class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr == '(':
                    if i != ")":
                        return False
                if curr == '{':
                    if i != "}":
                        return False
                if curr == '[':
                    if i != "]":
                        return False
        if stack:
            return False
        else:
            return True
