# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MergeKSortedLists(object):
    def mergeKLists(self, lists):
        """
        Problem state: Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
        type lists: List[ListNode]
        return type: ListNode
        Idea: Gather all input element to the array in the while loop -> sort -> generate the link list we return 
        """
        LinkList_return = None
        list_tmp = []
        #Gather all input element to the array in the while loop
        while len(lists) > 0:
            for each_id in reversed(range(len(lists))):
                if lists[each_id] == None:
                    lists.pop(each_id)
            if len(lists)>0:
                for each_sub in range(len(lists)):
                    list_tmp.append(lists[each_sub])
                    lists[each_sub] = lists[each_sub].next
        #sort by .val 
        #( lambda key is general for all custom object and array in the matrix, reverse the result is determined by reverse key )
        list_tmp.sort(key=lambda x: x.val, reverse=False)
        #Regenerate a new link list from the last to the first of the array we gathered
        for each_id in reversed(range(len(list_tmp))):
            list_tmp[each_id].next = LinkList_return
            LinkList_return = list_tmp[each_id]
        return LinkList_return
