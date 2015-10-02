class ReverseBit(object):
    def reverseBits(self, n):
        """
        Problem state : Reverse bits of a given 32 bits unsigned integer.
        ( For example: 43261596 as 00000010100101000001111010011100, return 964176192 as 00111001011110000010100101000000 )
        type n: int
        rtype: int
        Idea : Transfer to bit string by format -> reverse -> Transfer back to Integer
        """
        #Transfer to bit string
        #{}.format(n) solution : (reference from stackoverflow.com)
        #{} -> places a variable into a string
        #0 -> takes the variable at argument position 0
        #: -> adds formatting options for this variable (otherwise it would represent decimal 6)
        #032 -> formats the number to 32 digits zero-padded on the left
        #b -> converts the number to its binary representation
        str_rev = '{0:032b}'.format(n)[::-1]
        
        return int(str_rev, 2)