def sum_two_lists(self, llist):
        rtn = LinkedList()
        llist1 = self.head
        llist2 = llist.head

        total = 0
        carry = 0

        while llist1 and llist2:
            total = llist1.data + llist2.data + carry 
            rtn.append(total % 10)
            carry = total // 10

            llist1 = llist1.next
            llist2 = llist2.next


        while llist1:
            total = llist1.data + carry
            rtn.append(total % 10)
            carry = total // 10
            llist1 = llist1.next
        
        while llist2:
            total = llist2.data + carry
            rtn.append(total % 10)
            carry = total // 10
            llist2 = llist2.next

        return rtn
        