class isPalindrome(object):
    def isPalindrome(self, x):
        """
        Problem state : Check an input value if it is Palindrome Number or not
        Type x: int
        Return type: bool
        Idea : int to str -> copy and reverse one of strings -> compare the 2 strings
        """
        #Set default output
        b_RtResult = False
        #Transfer the input to string
        str_x = str(x)
        #Reverse the string and store in a new value
        str_x_rev = str_x[::-1]
        #Compare, if equal output true or output false
        if str_x == str_x_rev:
            b_RtResult = True
        return b_RtResult