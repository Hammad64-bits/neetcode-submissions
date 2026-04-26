class Solution:

    # array of integers nums
    # return the length of the longest consecutive sequence of elements that can be formed.

    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 1
        if len(nums) == 0: return 0
        seen = set(nums)
        start = 0
        longest = 0
        for num in nums:
            count = 1
            if num - 1 not in seen:
                start = num
                print('entering while loop with start', start)
                while start + 1 in seen:
                    print('num', num,'start ', start, 'count', count)
                    start += 1
                    count += 1
                longest = max(longest, count)
                print('exited while loop')


        print(seen)
        
        return longest

        