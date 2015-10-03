class FindPeakElement(object):
    def findPeakElement(self, nums):
        """
        Problem state : Given an input array where num[i] != num[i+1], find a peak element and return its index.
                        The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
                        For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
        type nums: List[int]
        return type: int
        Idea : Length check -> Find Max number -> Find the index of the Max number
        """
        #Get the length of the input list
        i_len_list = len(nums)
        i_rtVal = -1
        if i_len_list == 0:
            #If empty list, return -1
            pass
        elif i_len_list == 1:
            #If list with only one value, return 0 as the only-index which available
            i_rtVal = 0;
        else:
            #Find Max value by Copied-Sort so we can get last one as the Max value without change the original's order
            i_max_val = sorted(nums)[i_len_list-1]
            #Find the index of the Max value by for loop and stop when find out
            for each_num in range(i_len_list):
                if nums[each_num] == i_max_val:
                    i_rtVal = each_num
                    break
        return i_rtVal