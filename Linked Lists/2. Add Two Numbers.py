# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def carry(i, l1, l2):
    if i < 0:
        return 0
    else:
        return int(10 <= l1[i] + l2[i] + carry(i-1, l1, l2))

class Solution:
    def addTwoNumbers(self, l1, l2):

        maxlistlen= max(len(l1), len(l2))
        minlistlen = min(len(l1), len(l2))
        l1max = False
        if len(l1) > len(l2):
            l1max = True
        else:
            l2max = True
        ans = []

        for i in range(maxlistlen):
            print(i, minlistlen)
            if i >= minlistlen:
                if l1max:
                    print(l1[i])
                    ans.append(l1[i])
                else:
                    print(l2[i])
                    ans.append(l2[i])
            else:
                print(carry(i, l1, l2))
                ans.append(l1[i] + l2[i] + carry(i, l1, l2))
        return ans

l1 = [2,4,3]
l2 = [5,6,4]
sol = Solution()
print(sol.addTwoNumbers(l1, l2))