class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""

        for index in range(len(strs[0])):
            for word in strs:
                if index >= len(word):
                    return prefix
                if word[index] != strs[0][index]:
                    return prefix

            prefix += strs[0][index]
        return prefix
