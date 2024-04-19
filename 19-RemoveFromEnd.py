# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    count = 0
    dum = ListNode(-1)

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # use list to get n'th node
        ## head1 = ListNode(-1)
        # d1 = head
        # l = []
        # while d1:
        #     l.append(d1)
        #     d1 = d1.next
        # lenth = len(l)
        # if lenth == n:
        #     head = head.next
        # else:
        #     l[len(l)-n-1].next = l[len(l)-n-1].next.next
        # return head

        # method2 :ust rever
        if not head:
            return head
        head.next = self.removeNthFromEnd(head.next, n)
        self.count += 1
        if self.count == n:
            self.dum = head
            return head.next
        else:
            return head


if __name__ == '__main__':
    solution = Solution()
    l = [1,4,3,2,5,2]
    head = ListNode(l[0])
    cur = head
    for i in range(1,len(l)):
        n = ListNode(l[i])
        cur.next = n
        cur = cur.next

    r = solution.removeNthFromEnd(head,3)

    while r:
        print(r.val,end="")
        r = r.next
    print('\n ')
    # print the deleted node info
    print(solution.dum.val)

