class MoveZeroes(object):
    def moveZeroes(self, nums):
        """
        Problem state: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
                       For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
                       Note that You must do this in-place without making a copy of the array and minimize the total number of operations.
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Idea: Search from the end to start, pop from the location if 0 identified and append 0 back to the list
        """
        i_Len = len(nums)
        
        for each_id in range(i_Len):
            #To easily maintain the order of non-zero item in the list, we scan from the end
            if nums[i_Len-1-each_id]==0:
                #Pop from the location
                nums.pop(i_Len-1-each_id)
                #Append 0 back to the list
                nums.append(0)