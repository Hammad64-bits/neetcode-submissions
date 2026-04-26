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


class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = []

        for i in range(len(nums)):

            product = 1

            for j in range(len(nums)):
                if j == i: continue
                product *= nums[j]
            arr.append(product)

        return arr
        