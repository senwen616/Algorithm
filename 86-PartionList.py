# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        phead1 = ListNode(-1)
        phead2 = ListNode(-1)
        cur1 = phead1
        cur2 = phead2
        # 还需一个虚拟节点，模拟当前head
        p = head
        while p:

            #  注意不能直接让head进行移动，需要先断开head 原始链接
            # 不能直接head = head.next
            if p.val < x:
                cur1.next = p
                cur1 = cur1.next
            else:
                cur2.next = p
                cur2 = cur2.next
            # clear p's next
            temp = p.next
            p.next = None
            p = temp
        cur1.next = phead2.next
        return phead1.next
if __name__ == '__main__':
    solution = Solution()
    l = [1,4,3,2,5,2]
    head = ListNode(l[0])
    cur = head
    for i in range(1,len(l)):
        n = ListNode(l[i])
        cur.next = n
        cur = cur.next

    r = solution.partition(head,3)

    while r:
        print(r.val)
        r = r.next
