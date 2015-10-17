class PowerOfTwo(object):
    def isPowerOfTwo(self, n):
        """
        Problem state: Given an integer, write a function to determine if it is a power of two.
        type n: int
        return type: bool
        Idea: If n is power of two, which means first bit MUST be 1 and rest of other bits is 0 when transform to bit sting
              And n-1 will be first bit as 0, rest of others as 1 with the same length when transform to bit sting
              That means if we do n & n-1, we will get 0 in final
        """
        #Set default return value
        b_rtVal = False
        
        #Check if n is grater than 0, and return false if not
        if n<1:
            b_rtVal = False
        else:
            #Do the binary and between n and n-1
            if n & (n-1) == 0:
                b_rtVal = True
            else:
                b_rtVal = False
        
        return b_rtVal