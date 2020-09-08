# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
time: nlgn + nlgn
space: 2n
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        prehead = ListNode()
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(heap, node.val)
                node = node.next 
        node = prehead
        while len(heap) > 0:
            val = heapq.heappop(heap)
            node.next = ListNode()
            node = node.next 
            node.val = val
        return prehead.next
