class TwoSingleNumber(object):
    def singleNumber(self, nums):
        """
        Problem State: Given an array of integers, every element appears twice except for one. Find that single one.
                        (Your algorithm should have a linear runtime complexity. Try to implement it without using extra memory)
        type nums: List[int]
        return type: List[int]
        Idea : Generally, the concept is same with the SingleNumber. ( We DO NOT use the extra memory also )
               However the return is list not value only, and keep i_tmpCount and store in the list when find the only-item instead of change flag and break
        """
        list_rtVal = []
        #Length check, return [0,0] if the list empty
        if len(nums) == 0:
            list_rtVal.extend([0,0])
        #Length check, return the only element and 0 if the list length is 1
        elif len(nums)==1:
            list_rtVal.append(nums[0])
            list_rtVal.append(0)
        else:
            #Sort the list first
            nums.sort()
            #Set scan count, do the judge when the value is 1, otherwise turn the value to next by the order of 0 -> 1
            i_tmpCount = 1
            #Value of the last scanned
            i_tmp_Scan = nums[0]
            #We will start from the second element of the list, so initially we set count as 1 and i_tmp_Scan as the 1st element in the list
            for each_id in range(1,len(nums)):
                #When scan the even position, and the value not equal with the last one, 
                #store the last value(which already stored at the i_tmp_Scan) to return value, than break
                if (nums[each_id]!=i_tmp_Scan) and (i_tmpCount == 1):
                    #Store the value when identify any value as the single
                    list_rtVal.append(i_tmp_Scan)
                    #Replace the i_tmp_Scan as the current scan number
                    i_tmp_Scan = nums[each_id]
                    #Keep the flag so next scan target can be identified as the even element from the new start point
                    i_tmpCount = 1
                elif (nums[each_id]==i_tmp_Scan) and (i_tmpCount == 1):
                    #If equal than turn to next phase
                    i_tmpCount = 0
                elif i_tmpCount == 0:
                    #If add position, store the value to i_tmp_Scan and switch the value of i_tmpCount
                    i_tmpCount = 1
                    i_tmp_Scan = nums[each_id]
                else:
                    pass
            #When flag keeps in 1, which means the last single-item is the last one, add the last one to the list
            if i_tmpCount==1:
                list_rtVal.append(nums[len(nums)-1])
        return list_rtVal