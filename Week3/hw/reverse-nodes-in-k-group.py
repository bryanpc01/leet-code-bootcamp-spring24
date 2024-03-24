######################################################################################
# Given the head of a linked list, 
# reverse the nodes of the list k at a time, 
# and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, 
# in the end, should remain as it is.

# You may not alter the values in the list's nodes, 
# only nodes themselves may be changed.
######################################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        tail = None

        outHead = None

        while ptr:
            count = 0

            ptr = head

            # place ptr k nodes ahead
            while count < k and ptr:
                ptr = ptr.next
                count = count + 1

            # if there is k nodes counted reverse output
            if count == k:
                revHead = self.reverseListByK(head, k)

                if not outHead:
                    outHead = revHead

                if tail:
                    tail.next = revHead
                tail = head
                head = ptr

        # connect remaining nodes
        if tail:
            tail.next = head

        # return outputHead if there was some items reversed if not return original list
        if outHead:
            return outHead
        else:
            head 

    def reverseListByK(self, head, k):
        outHead = None
        ptr = head

        while k:
            # store next node in list
            next  = ptr.next

            # Reverse current node and place in the front of the output node
            ptr.next = outHead
            outHead = ptr
            
            # continue
            ptr = next
            k = k - 1 

        return outHead