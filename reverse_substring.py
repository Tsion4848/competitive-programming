class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        
        for i in range(len(s)):
            if (s[i] == '('):
                st.append(i)
            elif (s[i] == ')'):
                x = s[st[-1]:i + 1]
                s = s[:st[-1]] + x[::-1] + s[i + 1:]
                del st[-1]
          
        result = ""
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                result += (s[i])
        return result
