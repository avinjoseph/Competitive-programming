# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#! My Solution

from typing import List

#? I had used dictionary to count the occurance of each value and used again a for loop to find which occurance had come the most
#? Here i had not implement within O(1) space.
class MySolution:
    def majorityElement(self, nums: List[int]) -> int:                     
        count = 1
        store = {}
        for ele in nums:
            if ele in store:
                store[ele] = store[ele] + 1
            else:
                store[ele] = count
        large = 0
        result = 0
        for key in store:
            if store[key] > large:
                large = store[key]
                result = key

        return result


class LesserSolution:
    def majorityElement(self, nums:List[int]) -> int:
        count = {}
        res, MaxCount = 0,0
        for ele in nums:
            count[ele] = 1 + count.get(ele,0)
            res = ele if count[ele] > MaxCount else MaxCount
            MaxCount = max(MaxCount,count[ele])

        return res
    

sol = LesserSolution();
print(sol.majorityElement([2,2,1,1,1,2,2]))


#! Neet Code Solution Optimized to O(1) space

class Optimized:
    def majorityElement(self, nums:List[int]) -> int:
        res, count = 0,0        #? res stores the value and count increment with the occurance
        for i in nums:
            if count == 0:      #? Initially count is 0 so res will store the value
                res = i
                                                #? count increment when same value occurs
            count += (1 if i == res else -1)    #? count decrement when other values occur when it become 0 the next value will be set as res
        return res
    
sol = Optimized();
print(sol.majorityElement([2,2,1,1,1,2,2,3]))