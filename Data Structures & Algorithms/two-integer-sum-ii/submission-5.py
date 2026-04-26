# array of integers numbers
# sorted in non-decreasing order

# Return the indices (1-indexed)
#   of two numbers [index1, index2]
#       they add up to "target"  

# index1 and index2 cannot be equal
# therefore you may not use the same element twice.

# exactly one valid solution

# Your solution must use O(1) additional space.

# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # map = {}
        # for i, n in enumerate(numbers):
        #     if(map.get(n) is not None): continue //
        #     needed = target - n

        #     if needed in map:
        #         return [map.get(needed), i + 1]

        #     map[n] = i + 1

        # print(map)
        # return []

        # for i, n in enumerate(numbers):
        #     needed = target - n
        #     if needed in numbers:
        #         return [i + 1, numbers.index(needed) + 1]
        # return []

        left, right = 0, len(numbers) -  1

        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]

            if res > target:
                right -= 1
            else:
                left += 1


        return []

        