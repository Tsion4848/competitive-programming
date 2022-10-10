class Solution:
    def __init__(self):
        self.operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        for t in tokens:
            if t in self.operators:
                stack.append(self.operators[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))

        return stack[0]
#         exp = tokens.split()
#         st = []
        
#         for ex in exp:
#             if ex not in '/*+-':
#                 st.append(int(ex))
#             else:
#                 r = st.pop()
#                 l = st.pop()
                
#             if ex == '+':
#                 st.append(l + r)
#             if ex == '-':
#                 st.append(l - r)
#             if ex == '*':
#                 st.append(l * r)
#             if ex == '/':
#                 st.append(int(l / r))
#         return st.pop()
