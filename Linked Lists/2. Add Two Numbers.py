# Definition for singly-linked list.
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def build_LL(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head
"""
def add(val1, val2, carry):
    addsum = val1 + val2 + carry
    if addsum >= 10:
        carry = addsum // 10
        addsum -= 10 * carry
    else:
        carry = 0
    return addsum, carry

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]):
        carry = 0
        ans = ListNode(0)
        curr_ans = ans
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 or curr_l2 or carry:
            if curr_l1 and curr_l2:
                addsum, carry = add(curr_l1.val, curr_l2.val, carry)
                curr_l1 = curr_l1.next
                curr_l2 = curr_l2.next
            elif curr_l1:
                addsum, carry = add(curr_l1.val, 0, carry)
                curr_l1 = curr_l1.next
            elif curr_l2:
                addsum, carry = add(0, curr_l2.val, carry)
                curr_l2 = curr_l2.next
            else:
                addsum = carry
                carry = 0
            curr_ans.next = ListNode(addsum)
            curr_ans = curr_ans.next
        return ans.next

"""
sol = Solution()
l1 = build_LL([2, 4, 3])
l2 = build_LL([5, 6, 4])

curr = sol.addTwoNumbers(l1, l2)
while curr:
    print(curr.val, end=">")
    curr = curr.next
"""