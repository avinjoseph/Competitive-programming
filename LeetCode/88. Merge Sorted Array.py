# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# My Solution

from typing import List

class MySolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #Merged both the arrays into nums1
        count = 0
        for i in range(m,m+n):
            if count < n :
                nums1[i] =  nums2[count]
                count += 1

        #Sorrted the nums1 array
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                if nums1[j] < nums1[i]:
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp

        print(nums1)


execution = MySolution();
execution.merge([1,2,3,0,0,0],3,[2,5,6],3)


#NeetCode Solution

class NeetCode:
    def merge(self, nums1 : List[int], m : int, nums2 : List[int], n : int) -> None:

        #last index nums1
        last = m + n - 1

        #Since both the arrays are in ascending order we are checking the last values of both the array i.e which is the largest 
        #Then we append in the final index of the nums1 array

        #merge in reverse order
        while n > 0  and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1

            last -= 1

        #fill the nums1 with the leftover from nums2 array
        #there leftover of nums1 will be present in nums1 itself so we dont need to fill it.
        while n>0:
            nums1[last] = nums2[n]
            last, n = last-1, n-1


execution2 = NeetCode();
execution2.merge([1,2,3,0,0,0],3,[2,5,6],3)