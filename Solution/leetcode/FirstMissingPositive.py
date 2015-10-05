class FirstMissingPositive(object):
    def firstMissingPositive(self, nums):
        """
        Problem state : Given an unsorted integer array, find the first missing positive integer.
                        For example, given [1,2,0] return 3, and [3,4,-1,1] return 2.
        type nums: List[int]
        return type: int
        Idea : Sort the input array -> Scan all element -> Pass when value is non-positive -> 
                If any positive value large than previous value by one, replace the previous value by the current value, 
                otherwise, break and return the next of the previous value
                -> If the loop run out, return the the next of the last element of the array, which also as the previous value at that time
        """
        #Sort the input array
        nums.sort()
        #Set the previous value we will use by 0
        i_preNum = 0
        for each_num in nums:
            if each_num<=0:
                pass
            else:
                if each_num - i_preNum > 1:
                #If any positive value large than previous value by two or more, break
                    break
                else:
                #If any positive value large than previous value by one, replace the previous value by the current value
                    i_preNum = each_num
        #Return the next of the previous value
        return i_preNum+1