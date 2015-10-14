class NumberOf_1Bits(object):
    def hammingWeight(self, n):
        """
        Problem state : Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
                        For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
        type n: int
        return type: int
        Idea : We have 2 approaches
               (1)Transfer to binary bit string, than count by scan each character
               (2)Check the mod 2 value and count 1 if the value is 1, than replace the original vale with the quotient which is the original vale divided by 2.
                  Continue the loop until the original vale becomes 0.
        """
        i_count1 = 0
        '''
        str_inputBinary = '{0:032b}'.format(n)
        for each_id in range(32):
            if str_inputBinary[each_id] == '1':
                i_count1 = i_count1+1
        '''
        
        i_remain_n = n
        #Run the while loop until the original vale becomes 0
        while i_remain_n>=1:
            #Count 1 if the mod 2 value is 1
            if i_remain_n % 2 == 1:
                i_count1 = i_count1+1
            #Replace the original vale
            i_remain_n = int(i_remain_n/2)
        
        return i_count1