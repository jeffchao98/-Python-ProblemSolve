# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class SortList(object):
    def sortList(self, head):
        """
        Problem state: Sort a linked list in O(n log n) time using constant space complexity.
        type head: ListNode
        return type: ListNode
        Idea: Gather in the list -> sort by .val -> regenerate a new link list from the last to the first of the array we gathered
        """
        LinkList_return = None
        list_tmp = []
        while head!=None:
            #Gather in the list
            list_tmp.append(head)
            head = head.next
        #sort by .val 
        #( lambda key is general for all custom object and array in the matrix, reverse the result is determined by reverse key )
        list_tmp.sort(key=lambda x: x.val, reverse=False)
        #Regenerate a new link list from the last to the first of the array we gathered
        for each_id in reversed(range(len(list_tmp))):
            list_tmp[each_id].next = LinkList_return
            LinkList_return = list_tmp[each_id]
            
        
        return LinkList_return