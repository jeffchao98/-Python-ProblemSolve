class GetMinInList(object):
    def findMin(self, nums):
        """
        Problem State : Suppose a sorted array is rotated at some pivot unknown to you beforehand.
        (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)
        type nums: List[int]
        return type: int
        Idea : Sort -> Get the first number + length check
        Common:
        (Update 151003-0944)accepted if duplicated include
        """
        nums.sort()
        if len(nums)>0:
            return nums[0]
        else:
            return 0