class SingleNumberFromTriple(object):
    def singleNumber(self, nums):
        """
        Problem state : Given an array of integers, every element appears three times except for one. Find that single one.
                        (Note:Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?)
        type nums: List[int]
        return type: int
        Idea : Same with the SingleNumber problem, we just need modify the second if-else condition 
                in the for loop so that adapt the appears three times condition
        """
        i_rtVal = 0
        #Length check, return None if the list empty
        if len(nums) == 0:
            i_rtVal = None
        #Length check, return the only element if the list length is 1
        elif len(nums)==1:
            i_rtVal = nums[0]
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
                    i_rtVal = i_tmp_Scan
                    #Mark so we can identify when out of the loop
                    i_tmpCount = -1
                    break
                elif (nums[each_id]==i_tmp_Scan) and (i_tmpCount < 3):
                    #If equal than turn to next phase
                    i_tmpCount = int((i_tmpCount+1)%3)
                elif i_tmpCount == 0:
                    #If add position, store the value to i_tmp_Scan and switch the value of i_tmpCount
                    i_tmpCount = 1
                    i_tmp_Scan = nums[each_id]
                else:
                    pass
            #When non-mark after loop finished, take the last one of the list as the return value
            if i_tmpCount!=-1:
                i_rtVal = nums[len(nums)-1]
        return i_rtVal        