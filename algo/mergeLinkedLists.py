# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
	p2 = headTwo
	prev = None
	
	while p1 and p2:
		if p1.value < p2.value:
			prev = p1
			p1 = p1.next
		else:
			if prev:
				prev.next = p2
			prev = p2
			p2 = p2.next
			prev.next = p1
	
	if p1 is None:
		prev.next = p2
	
	return headOne if headOne.value < headTwo.value else headTwo
