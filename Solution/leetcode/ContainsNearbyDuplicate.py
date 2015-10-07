class ContainsNearbyDuplicate(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Problem state : Given an array of integers and an integer k, 
                        find out whether there are two distinct indices i and j in the array 
                        such that nums[i] = nums[j] and the difference between i and j is at most k.
        type nums: List[int]
        type k: int
        return type: bool
        Idea : Do length check, return false if the length is 0 or 1 -> Create a dictionary -> 
               Scan all elements, 
               (1)add new if the element not contain in the dictionary
               (2)If contains, compare the different between the value and the current scan id, than update the dictionary value after compare
                  (a)Update the result as False if the different grater than k
                  (b)Update the result as True if the different smaller than k or equal
                -> Return the result
        """
        dic_tmp = {}
        b_result = False
        i_len_input = len(nums)
        #Do length check
        if i_len_input > 1:
            for each_id in range(i_len_input):
                if nums[each_id] in dic_tmp:
                #If contains, compare the different between the value and the current scan id
                    if abs(dic_tmp[nums[each_id]] - each_id)>k:
                        #Update the result as False if the different grater than k
                        b_result = False
                    else:
                        #Update the result as True if the different smaller than k or equal
                        b_result = True
                else:
                    pass
                #Add new if the element not contain in the dictionary, array value as the dictionary ID, array ID as the dictionary value
                #Update if the element DO contain in the dictionary, however after the different check complete
                dic_tmp[nums[each_id]] = each_id
        else:
            pass
        return b_result