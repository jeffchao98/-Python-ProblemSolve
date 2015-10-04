class RotateArray(object):
    def rotate(self, nums, k):
        """
        Problem state : Rotate an array of n elements to the right by k steps. 
                        For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        type nums: List[int]
        type k: int
        return type: void Do not return anything, modify nums in-place instead.
        Idea : Length check -> Continue if the length grater than 1 -> New array -> Get the mod value -> copy the last elements to new array -> copy the rest of elements to new array
                -> copy the new array back to array nums
        Common : Without the mod value get feature, the test runtime is 76ms in 33 test cases,
                with the feature, the worst test runtime is 160ms in 33 test cases, average is 85ms.
        """
        #Length check
        i_len_nums = len(nums)
        #Continue if the length grater than 1, otherwise just keep
        if i_len_nums < 2:
            pass
        else:
            #New array created
            list_tmp = []
            #Get the mod value in case the k grater than the array length -> However, 
            #the characteristic of Python no need this, just reference for the case of transfer to other language
            #If without it, the runtime will become 76ms in 33 test cases of leetcode
            true_k = k % i_len_nums
            #Copy the last true_k elements to new array
            for num in range(i_len_nums-true_k, i_len_nums):
                list_tmp.append(nums[num])
            #Copy the rest of elements to new array
            for num in range(i_len_nums-true_k):
                list_tmp.append(nums[num])
            #Copy the new array back to array nums
            for num in range(i_len_nums):
                nums[num] = list_tmp[num]