class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        write = 0

        for i in nums:
            if i != 0:
                nums[write] = i
                write += 1
        for j in range(write, len(nums)):
            nums[j] = 0