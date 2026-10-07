class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        
        for number in nums:
            if number != val:
                nums[pointer] = number
                pointer += 1
        return pointer