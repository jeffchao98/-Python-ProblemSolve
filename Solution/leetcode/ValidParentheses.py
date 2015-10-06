class ValidParentheses(object):
    def isValid(self, s):
        """
        Problem State : Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
                        The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        type s : str
        return type : bool
        Idea : Generate a list with only one element " " and a dictionary, place all element as Problem State described in the dictionary, for every item pair, 
                place the prefix part as id and suffix part as value -> 
                Length check, if odd return FALSE -> 
                Compare every element with the dictionary -> 
                (1)if found which means it is prefix part (id), than stack the suffix part in the list we generated before  
                (2)if no found, which means it is suffix part (value), compare the last element of the list, pop the last element if equal, otherwise return FALSE
                Compare complete, the list should only have the element as we created begin, if not ( length > 1 ), return FALSE->
                If go through to the end, return TRUE
                
        """
        #Create default return value
        b_rtVal = True
        #Generate a dictionary, place all element as Problem State described in the dictionary, for every item pair, 
        #place the prefix part as id and suffix part as value
        dic_varify = {'(':')', '{':'}', '[':']' }
        #Generate a list with only one element " "
        list_stack = [" "]
        #Length check, if odd return FALSE ( there's no possible generate pairs if the length is 2n+1 )
        if int(len(s)%2)==0:
            for each_num in range(len(s)):
                #Compare every element with the dictionary
                if s[each_num] in dic_varify:
                    #If found which means it is prefix part (id)
                    i_tmp_getChr = dic_varify[s[each_num]]
                    #stack the suffix part in the list
                    list_stack.append(i_tmp_getChr)
                else:
                    #If no found, which means it is suffix part (value), compare the last element of the list
                    if s[each_num] == list_stack[len(list_stack)-1]:
                        #pop the last element if equal ( two different closet elements belong to the same pair )
                        list_stack.pop()
                    else:
                        #return FALSE if non-equal
                        b_rtVal = False
                        break
        else:
            b_rtVal = False
        #If the length of the list is grater than 1, return FALSE ( i.e. '{[('  )
        if len(list_stack)!=1:
            b_rtVal = False
        return b_rtVal