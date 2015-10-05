class ExcelSheetColumnNumber(object):
    def gCO(self, cha_input):
        #Get the order of the char ( 0 ~ 25 )
        #In case lower case input, we should transfer any input to upper case
        return ord(cha_input.upper())-ord('A')
    def titleToNumber(self, s):
        """
        Problem state : Given a column title as appear in an Excel sheet, return its corresponding column number.
        type s: str
        return type: int
        Idea : Scan whole string from left to right, Get the char order by using ord([input])-ord('A')+1, 
                than calculate by [previous result]*26+[current] until last char scanned 
        """
        rtVal=0
        for each_num in range(len(s)):
            #Multiplex previous result by 26, plus current char's order and 1 ( A as 1 )
            rtVal = rtVal*26+self.gCO(s[each_num])+1
        return rtVal