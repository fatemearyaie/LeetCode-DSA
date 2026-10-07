class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
            }

        for letter in s:
            if letter in pairs.values():
                stack.append(letter)
            if letter in pairs.keys():
                if not stack:
                    return False
                if stack[-1] != pairs[letter]:
                    return False
                stack.pop()
        return not stack