class AddDigits(object):
    def addDigits(self, num):
        """
        Problem stste : Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
        ( For example:Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it. )
        type num: int
        return type: int
        Idea : Without recursive approach, we scan the input value from highest bit and plus each digit frequently.
               When the sum grater than 10, we should minus 9 ( also means minus 10 and plus 1 ), than proceed to scan next digit
        """
        i_rtVal = 0
        #Value check, direct return if the input value less than 10 ( only 1 digit )
        if num<10:
            i_rtVal = num
        else:
            #Transfer the input value to string
            str_num = str(num)
            #Go scan for each digit from highest one
            for each_id in range(len(str_num)):
                #When digit scanned, add the digit to return value
                i_rtVal = i_rtVal + ord(str_num[each_id])-ord('0')
                #If the return value grater than 9, minus 10 and plus 1
                if i_rtVal>9:
                    i_rtVal = i_rtVal-10+1
                else:
                    pass
        return i_rtVal