class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxim = 0

        for i in nums:
            if i == 1:
                count += 1
                if count >= maxim:
                    maxim = count
            else:
                count = 0
        return maxim