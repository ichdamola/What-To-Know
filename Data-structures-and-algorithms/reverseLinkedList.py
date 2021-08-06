class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        res = str(self.value)
        if self.next:
            res += str(self.next)
        return res

class Solution:
    def reverse(self, head: Node) -> Node:
        cur = head
        prev = None

        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp 
        return prev

linked_list = Node(1,Node(2, Node(3, Node(4, Node(5, None)))))
print(linked_list)
print(Solution().reverse(linked_list))
        