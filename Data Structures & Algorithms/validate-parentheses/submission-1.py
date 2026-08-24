class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "{":"}", "[":"]"} 
        stack = []
        for char in s:
            if char in d: #checks if char is a key in the dict
                stack.append(char)
            else: 
                if stack == [] or d[stack.pop()] != char:
                    return False
        return True if stack == [] else False
