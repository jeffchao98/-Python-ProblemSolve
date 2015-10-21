class LengthOfLastWord(object):
    def lengthOfLastWord(self, s):
        """
        Problem State: Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
                       return the length of last word in the string. If the last word does not exist, return 0.
                       Note: A word is defined as a character sequence consists of non-space characters only.
        type s: str
        return type: int
        Idea: remove the space from both side of the string, split and get the last "word", return the length
        """
        i_lenS = len(s)
        i_rtLen = 0
        if i_lenS == 0:
            pass
        else:
            #Remove the space from both side of the string
            s=s.strip()
            if ' ' in s:
                #split and get the last "word"
                list_tmp = s.split(' ')
                str_last = list_tmp[len(list_tmp)-1]
                i_rtLen = len(str_last)
                pass
            else:
                i_rtLen = len(s)
        return i_rtLen