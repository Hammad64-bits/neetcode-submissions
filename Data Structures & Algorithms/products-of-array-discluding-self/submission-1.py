# Given an integer array nums

# return an array output

#  where output[i] is the product of all the elements of nums 

# except nums[i].

# plan A

# 1. loop through nums

# 2. loop through rest of the elements except nums[i]

# 3. push it to the new array

# 4. return array

# plan B

# 1. loop through nums and get total product

# 2. loop again, divide product/nums[i] push to array and return

    # 2.1. what if the product is 0?


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        prefix = 1
        for i in range(n):
            arr[i] *= prefix
            prefix *= nums[i] 
        postfix = 1
        for i in range(n - 1, -1, -1):
            arr[i] *= postfix
            postfix *= nums[i]
        return arr
        