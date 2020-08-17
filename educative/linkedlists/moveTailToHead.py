    def move_tail_to_head(self):

        head = node = prev = self.head

        if not node.next:
            return

        while node.next:
            prev = node 
            node = node.next

        prev.next = None
        node.next = head 
        self.head = node