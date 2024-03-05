#################################################################
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two
# endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
##################################################################

# We currently know two techniques, two pointer and sliding window.
# In this problem, I think two pointer works best

def maxArea(height) -> int:
    # pointer to the start and end
    start = 0
    end = len(height) - 1

    max_area = 0
    for i in range(len(height)):
        curr_area = (end - start) * min(height[start], height[end])
        
        max_area = max(max_area, curr_area)

        if height[start] > height[end]:
            end -= 1
        else: 
            start += 1

    return max_area
