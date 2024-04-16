#################################
# Given an integer array nums and an integer k, 
# return the kth largest element in the array.
#################################

def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]
