# Definition for singly-linked list.
class Listnode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def build_LL(arr):
    if not arr:
        return None

    head = Listnode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = Listnode(val)
        current = current.next

    return head


def build_carry_list(l1, l2, carry_list, llen):
    curr_l1 = l1
    curr_l2 = l2
    for _ in range(llen):
        carry_list.insert(0, curr_l1.val + curr_l2.val)
        curr_l1 = curr_l1.next
        curr_l2 = curr_l2.next

    curr_carried = 0
    for i in range(len(carry_list)):
        curr_carried = int(carry_list[i] + curr_carried > 10)
        carry_list[i] = curr_carried


class Solution:
    def addTwoNumbers(self, l1: [Listnode], l2: [Listnode]):
        ans = []

        curr = l1
        lenl1 = 0
        l1last = None
        while curr:
            lenl1 += 1
            l1last = curr
            curr = curr.next

        curr = l2
        lenl2 = 0
        l2last = None
        while curr:
            lenl2 += 1
            l2last = curr
            curr = curr.next

        max_len = max(lenl1, lenl2)
        for d in range(max_len - lenl1):
            l1last.next = Listnode(0)
            l1last = l1last.next
        for d in range(max_len - lenl2):
            l2last.next = Listnode(0)
            l2last = l2last.next

        carry = build_carry_list(l1, l2, [], max_len)

'''
def print_LL(LL):
    curr = LL
    while curr:
        print(curr.val, end = ">")
        curr = curr.next
    print(" ")

l1 = build_LL([2, 4])
l2 = build_LL([5, 6, 4])
curr = l1
lenl1 = 0
l1last = None

while curr:
    lenl1 += 1
    l1last = curr
    curr = curr.next

curr = l2
lenl2 = 0
l2last = None
while curr:
    lenl2 += 1
    l2last = curr
    curr = curr.next

max_len = max(lenl1, lenl2)
for d in range(max_len - lenl1):
    l1last.next = Listnode(0)
    l1last = l1last.next
for d in range(max_len - lenl2):
    l2last.next = Listnode(0)
    l2last = l2last.next

#print_LL(l1)
#print_LL(l2)

print(build_carry_list(l1, l2, [], max_len))
'''

carry_list = [4, 10, 9]
curr_carried = 0
for i in range(len(carry_list)):
    curr_carried = int(carry_list[i] + curr_carried >= 10)
    carry_list[i] = curr_carried

print(carry_list)