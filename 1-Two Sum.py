class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, number in enumerate(nums):
            x = target - number
            if x in seen:
                return (seen[x], index)
            seen[number] = index