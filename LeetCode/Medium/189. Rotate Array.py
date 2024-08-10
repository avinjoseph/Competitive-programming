# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 
from typing import List


#! My Solution
class MySolution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        ex nums = [1,2,3,4,5] k=2 
        step 1 :- add elements to K + places
        arr = [_,_,1,2,3]
        step 2 : add next element to the first places but using modulus
        arr = [4,5,1,2,3]
        step 3 :- copy the arr array to nums.
        """
        arr = [i for i in range(len(nums))]         #? Create a empty array of same length
        k = k % len(nums)                           #? k element can be greater than length of array. if its greater the rotation will be same no diff
        for i in range(len(nums)):
            index = i+k                             #? Each element is shifted to k+ places 
            if index < len(nums):
                arr[index] = nums[i]
            else:
                index = index % len(nums)           #? modulus operator is used to get the proper inddex which was out of bound
                arr[index] = nums[i]                

        
        return arr


result = MySolution();
print(result.rotate([1,2,3,4,5,6,7],3))



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        ex nums = [1,2,3,4,5] k=2 
        step 1 :- reverse the entire array
        nums = [5,4,3,2,1]
        step 2 : reverse first section of array upto k
        nums = [4,5,3,2,1]
        step 3 :- reverse second section of array upto len(nums)-1
        nums = [4,5,1,2,3]

        """
        k = k % len(nums)
        l,r = 0, len(nums) - 1          #? assigning the values
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]         #? In python we dont need temp value for swappping
            l, r = l+1, r-1

        l,r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        l,r = k, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1