class MergeSortedArray(object):
    def merge(self, nums1, m, nums2, n):
        """
        Problem state : Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. 
                        Assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
                        The number of elements initialized in nums1 and nums2 are m and n respectively.
        type nums1: List[int]
        type m: int
        type nums2: List[int]
        type n: int
        return type: void Do not return anything, modify nums1 in-place instead.
        Idea : Create new list -> Copy all available items from each list -> Sort the new list -> Replace the leading m+n element of num2 by the new list
        """
        #Create new list
        list_out = []
        #Copy all available items from the list nums1
        for each_num in range(m):
            list_out.append(nums1[each_num])
        #Copy all available items from the list nums2
        for each_num in range(n):
            list_out.append(nums2[each_num])
        #Sort the new list
        list_out.sort()
        #Replace the leading m+n element of num2 by the new list
        for each_num in range(m+n):
            nums1[each_num]=list_out[each_num]