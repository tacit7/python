TreeNode()

def addTwoNumbers(l1, l2, c):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
        """
    val1 = (l1.val or 0)
    val2 = (l2.val or 0)
    this_val = val1 + val2 + c
    c = val // 10
    sum = ListNode(val % 10)

    if (l1.next == None and l2.next == None):
        return sum
    elif l1.next == None and l2.next != None:
        l1.next = ListNode(0)
        sum.next = self.addTwoNumbers(l1.next, l2.next, c)
    elif l1.next != None and l2.next == None:
        l2.next = ListNode(0)
        sum.next = self.addTwoNumbers(l1.next, l2.next, c)
    else:
        sum.next = self.addTwoNumbers(l1.next, l2.next, c)
