class SpiralMatrixB(object):
    def generateMatrix(self, n):
        """
        Problem State: Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
                       For example, Given n = 3, you should return the following matrix:
                        [
                         [ 1, 2, 3 ],
                         [ 8, 9, 4 ],
                         [ 7, 6, 5 ]
                        ]
        type n: int
        return type: List[List[int]]
        Idea: Rough version, generate the static space first, start from (0,0) and right direction, 
              however change the direction when the next block out of range or not equal as 0
               order of the directions: right -> down -> left -> up
        """
        
        list_return=[]
        #If given n is not grater than 0, return a empty list
        if n<=0:
            return list_return
        #Generate the static space first by given n
        for each_id in range(n):
            list_tmpSub=[]
            for each_id in range(n):
                list_tmpSub.append(0)
            list_return.append(list_tmpSub)
        
        #start from (0,0), keep record last position we do edit
        i_doX = 0
        i_doY = 0
        i_countMark = 0
        
        b_KeepLoop = True
        
        i_way = 1
        
        b_ChangeWay=False
        
        while b_KeepLoop:
            #mark if last time we do not change direction
            if b_ChangeWay:
                b_ChangeWay=False
                pass
            else:
                i_countMark = i_countMark+1
                list_return[i_doY][i_doX] = i_countMark
            
            #search
            i_nextX = i_doX
            i_nextY = i_doY
            
            
            #Go forward by the same direction, however stop and proceed to next direction if the next block out of range or not equal as 0
            #right
            if i_way == 1:
                if i_nextX+1 in range(n) and list_return[i_nextY][i_nextX+1] == 0:
                    i_doX = i_nextX+1
                else:
                    b_ChangeWay = True
            #down
            elif i_way == 2:
                if i_nextY+1 in range(n) and list_return[i_nextY+1][i_nextX] == 0:
                    i_doY = i_nextY+1
                else:
                    b_ChangeWay = True
            #left
            elif i_way == 3:
                if i_nextX-1 in range(n) and list_return[i_nextY][i_nextX-1] == 0:
                    i_doX = i_nextX-1
                else:
                    b_ChangeWay = True
            #up
            else:
                if i_nextY-1 in range(n) and list_return[i_nextY-1][i_nextX] == 0:
                    i_doY = i_nextY-1
                else:
                    b_ChangeWay = True
            #change the direction if we can not keep going
            if b_ChangeWay:
                if i_nextX+1 in range(n) and list_return[i_nextY][i_nextX+1] == 0:
                    i_way = 1
                elif i_nextY+1 in range(n) and list_return[i_nextY+1][i_nextX] == 0:
                    i_way = 2
                elif i_nextX-1 in range(n) and list_return[i_nextY][i_nextX-1] == 0:
                    i_way = 3
                elif i_nextY-1 in range(n) and list_return[i_nextY-1][i_nextX] == 0:
                    i_way = 4
                else:
                    #Stop the loop if no available next-step four directions
                    b_KeepLoop = False

        return list_return