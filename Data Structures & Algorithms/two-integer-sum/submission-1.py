class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = dict()

        for i, num in enumerate(nums):
            
            needed = target - num
            if needed in lookup: return [lookup[needed] ,i]
            lookup[num] = i
        
        