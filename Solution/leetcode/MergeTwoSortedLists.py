# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MergeTwoSortedLists(object):
    def mergeTwoLists(self, l1, l2):
        """
        Problem state: Merge two sorted linked lists and return it as a new list. 
                       The new list should be made by splicing together the nodes of the first two lists.
        type l1: ListNode
        type l2: ListNode
        return type: ListNode
        Idea: Because we have two sorted link list, we just need gather the elements in the array by the merge sort
              (Scan the values of each head -> peak the smaller one-the next will take place -> regenerate a new link list from the last to the first of the array we gathered)
        """
        b_DoWhile = True
        ListNode_Return = None
        List_tmp = []
        while b_DoWhile:
            #The while loop will stop when both l1 and l2 are empty
            if l1==None and l2==None:
                b_DoWhile = False
            #If only l1 empty, then just pick the first element of l2 in every loop
            elif l1==None:
                List_tmp.append(l2)
                l2 = l2.next
            #If only l2 empty, then just pick the first element of l1 in every loop
            elif l2==None:
                List_tmp.append(l1)
                l1 = l1.next
            else:
                #Scan the first elements, then pick smaller one
                i_val1 = l1.val
                i_val2 = l2.val
                if i_val1>i_val2:
                    List_tmp.append(l2)
                    l2 = l2.next
                else:
                    List_tmp.append(l1)
                    l1 = l1.next
        #Regenerate a new link list from the last to the first of the array we gathered
        for each_id in reversed(range(len(List_tmp))):
            List_tmp[each_id].next = ListNode_Return
            ListNode_Return = List_tmp[each_id]
        return ListNode_Return
