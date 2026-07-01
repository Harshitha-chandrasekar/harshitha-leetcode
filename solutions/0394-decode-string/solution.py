class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        st = ""
        stack = []

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                stack.append([num,st])
                num = 0
                st = ""
            elif char == ']':
                prevn,prevs = stack.pop()
                st = prevs + (st*prevn)
            else:
                st = st + char

        return st
