def reverseLinkedList(head):
	node = head
	prev = None
	
    while node:
		node.next, prev, node = prev, node, node.next
	
	return prev