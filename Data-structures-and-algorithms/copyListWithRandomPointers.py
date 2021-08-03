class Node:
    def __init__(self, x, next, random) -> None:
        self.val = x
        self.next = next
        self.random = random
        
    def copyRandomList(self, head, Node):
        dummy = new = Node(-1)
        cur = head
        old_new = {}

        while cur:
            new.next = Node(cur.val)
            old_new[cur] = new.next
            cur = cur.next
            new = new.next
        cur = head
        new = dummy.next

        while cur:
            if cur.random:
                new.random = old_new[cur.random]
            new = new.next
            cur = cur.next
        return dummy.next