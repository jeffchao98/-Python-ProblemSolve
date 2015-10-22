class ValidAnagram(object):
    def isAnagram(self, s, t):
        """
        Problem State: Given two strings s and t, write a function to determine if t is an anagram of s.
                       For example, s = "anagram", t = "nagaram", return true. s = "rat", t = "car", return false.
                       Note that You may assume the string contains only lower case alphabets.
        type s: str
        type t: str
        return type: bool
        Idea: Use dictionary, record the alphabets appears status in s, and compare with t
        """
        b_rtRes = False
        #Get the length of s and t
        i_lenS = len(s)
        i_lenT = len(t)
        dic_tmpRec = {}
        #If s and t not in same length, t IS NOT an anagram of s.
        if i_lenS != i_lenT:
            pass
        else:
            #Record the alphabets appears status of s by using dictionary
            for each_id in range(i_lenS):
                if s[each_id] in dic_tmpRec:
                    dic_tmpRec[s[each_id]] = dic_tmpRec[s[each_id]]+1
                else:
                    dic_tmpRec[s[each_id]] = 1
            #Compare the record with t, which means minus the count to records in the dictionary
            for each_id in range(i_lenT):
                if t[each_id] not in dic_tmpRec:
                    break
                else:
                    if dic_tmpRec[t[each_id]] == 1:
                        del dic_tmpRec[t[each_id]]
                    else:
                        dic_tmpRec[t[each_id]] = dic_tmpRec[t[each_id]]-1
            #If nothing remains in the dictionary, it deserved TURE, otherwise False
            if len(dic_tmpRec)==0:
                b_rtRes = True
        return b_rtRes