def is_circular_linked_list(self, input_list):
    fast = slow = input_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False