class ReverseInt(object):
    def reverse(self, x):
        """
        Problem state : Reverse digits of an integer.(Example1: x = 123, return 321, Example2: x = -123, return -321)
        type x: int
        return type: int
        Idea : Absolute the value -> Transfer to String -> Reverse string -> Transfer back to Integer and put back '-' if less than 0
        -> replace as 0 if the result out of Integer range
        Common : In leetcode verification function, the result MUST in the range between 2147483647 and -2147483648 or regard as 0,
                 however, we still can transfer and output even out of the range and with out the range check process
                 ( perhaps transfer to long automatically ) 
                 --> Is this necessary that add the range check for prevent the overflow which might be happen?
        """
        str_output = ''
        #Absolute and transfer to string
        str_input = str(abs(x))
        i_output = 0
        #Reverse the string
        str_output = str_input[::-1]
        #Transfer back to Integer
        i_output = int(str_output)
        #Put back '-' if input less than 0
        if x<0:
            i_output = i_output*(-1)
        #Check the value belong in the range of Integer, set as 0 if not
        if i_output>2147483647:
            i_output = 0
        if i_output<-2147483648:
            i_output = 0
        
        return i_output