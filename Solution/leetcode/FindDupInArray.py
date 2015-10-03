class FindDupInArray(object):
    def findDuplicate(self, nums):
        """
        Problem state : Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
                        prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
                        find the duplicate one.
                        Note:
                        1.You must not modify the array (assume the array is read only).
                        2.You must use only constant, O(1) extra space.
                        3.Your runtime complexity should be less than O(n^2).
                        4.There is only one duplicate number in the array, but it could be repeated more than once.
        type nums: List[int]
        return type: int
        Idea : Copy and sort array -> scan and break if an element equals as the previous one
        """
        #Copied-Sort and store in another value so we can do sort without change the original's order
        list_num = sorted(nums)
        #Get the first one as the first compared item
        i_last = list_num[0]
        for id in range(1,len(list_num)):
            #If same as the last one, break 
            if list_num[id] == i_last:
                break
            #Otherwise, update the compared item
            else:
                i_last = list_num[id]
        return i_last