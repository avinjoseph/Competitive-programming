# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#! NeetCode Solution

from typing import List

#* Two pointer is used right pointer is used to iterate through the list

class NeetCode:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0, 0 

        while right < len(nums):
            count = 1                                     

            while right+1 < len(nums) and nums[right] == nums[right+1]:  #? check the next value and current value  same 
                count += 1                                               #? find the total count of occurance of the value in it by while loop
                right += 1

            for i in range(min(2,count)):                                #? min function is used if count is more than 3 then 2 values will be print else
                nums[left] = nums[right]                                 #? when the count is 1 then that number of values is printed
                left += 1                                                #? left pointer is used to keep track where the value need to be placed
            right += 1
        return left                                                      #? left pointer have the final number of values in the list


result = NeetCode();
print(result.removeDuplicates([0,0,1,1,1,1,2,3,3]))
            

#! Other Good Solution

class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        index = 1
        occurance = 1

        for i in range(1, len(nums)):                        #? Here total count of occurance is not taken it both values are same 
            if nums[i] == nums[i-1]:                         #? Then the second pointer i.e index value is replaced if occurance is less than 2
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index
    

result = Solution();
print(result.removeDuplicates([0,0,1,1,1,1,2,3,3]))