class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        Problem state : Given an array of integers, find if the array contains any duplicates. 
                        Your function should return true if any value appears at least twice in the array, 
                        and it should return false if every element is distinct.
        type nums: List[int]
        return type: bool
        Idea: sort -> check -> return true if duplicate founded
        """
        i_len = len(nums)
        b_result = False
        nums.sort()
        if i_len>1:
            for rach_id in range(1,i_len):
                if nums[rach_id] == nums[rach_id-1]:
                    b_result = True
                    break
                else:
                    pass
        else:
            pass
        return b_result