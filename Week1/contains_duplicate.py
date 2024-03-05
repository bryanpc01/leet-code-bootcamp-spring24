#####################################################
# Given an integer array nums, return true 
# if any value appears at least twice in the array, 
# and return false if every element is distinct.
####################################################


# We currently know two techniques, two pointer and sliding window. 
# In this problem, I think sliding window works best. 


# Solution using Sliding window technique.
def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort the elements of the array in place.
        nums.sort()
        # Use the sliding window technique to see if neighboring elements are equal
        k = 2 
        for i in range(len(nums) - k + 1):
            # if the length of elements in the window is less than the window size, there is a duplicate
            if len(set(nums[i:i+k])) < k:
                return True
        return False
