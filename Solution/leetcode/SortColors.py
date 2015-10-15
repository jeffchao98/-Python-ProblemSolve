class Solution(object):
    def sortColors(self, nums):
        """
        Problem state: Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, 
                       with the colors in the order red, white and blue.
                       Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
                       Note that you are not suppose to use the library's sort function for this problem.
        type nums: List[int]
        return type: void Do not return anything, modify nums in-place instead.
        Idea: If find 0, pop and insert to position 0; if find 2, pop and insert to the last position
              By we move 2 to last position, the index in the loop should be reduce by the count of 2 we moved,
              or some elements might be missed because the order rearranged.
        """
        #According to the problem state, the library's sort function is not available to use 
        #nums.sort()
        i_lenNums = len(nums)
        i_numsof2 = 0
        for each_id_o in range(i_lenNums):
            #Modify the scan index of the loop by reduce the count of 2 we moved
            each_id = each_id_o-i_numsof2
            #If find 0, pop and insert to position 0
            if nums[each_id] == 0:
                nums.pop(each_id)
                nums.insert(0,0)
            #If find 2, pop and insert to the last position
            elif nums[each_id] == 2:
                i_numsof2 = i_numsof2+1
                nums.pop(each_id)
                nums.insert(i_lenNums-1,2)
            else:
                pass