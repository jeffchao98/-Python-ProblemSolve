class ExcelSheetColumnTitle(object):
    def tChr(self, input):
        i_order = int((input-1)%26)
        return chr(i_order+ord('A'))
    def convertToTitle(self, n):
        """
        Problem state: Given a positive integer, return its corresponding column title as appear in an Excel sheet.
                        (Example. 1 -> A, 26 -> Z, 27 -> AA)
        type n: int
        return type: str
        Idea : 1. Use the chr() and ord() as well
               2. In case the values become non-int, force than become int by int() when calculate
               3. When divide 26 by 26, we expect the outcome will be 'Z' at final. However, the quotient is 1 and the reminder is 0, it will outcomes "AZ" or "A@" which is incorrect.
                  So we should not only -1 before get the reminder( reminder will be 25 in the case ), but -1 again before get quotient ( quotient will be 0 in the case )
                  And that DOES NOT means -2 to original value
        """
        str_rtVal =''
        quotient = n
        while quotient>0:
            str_rtVal = self.tChr(quotient)+str_rtVal
            quotient = int((quotient-1)/26)
        return str_rtVal