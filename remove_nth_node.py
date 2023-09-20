"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""
class Solution:
    def removeNthFromEnd(self, listNode, n: int):
        if n > len(listNode):
            exit()
        else:
            listNode.remove(listNode[-n])
            print(listNode[-n])
        return listNode
    
list=[1,3,5,6,4,3,9,0,11,12]
print(Solution().removeNthFromEnd(list,n))
