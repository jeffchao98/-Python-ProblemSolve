class SpiralMatrixA(object):
    def spiralOrder(self, matrix):
        """
        Problem state: Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
                       For example, given the following matrix:
                       [
                        [ 1, 2, 3 ],
                        [ 4, 5, 6 ],
                        [ 7, 8, 9 ]
                       ]
                       You should return [1,2,3,6,9,8,7,4,5].
        type matrix: List[List[int]]
        return type: List[int]
        Idea: We will "scan" the matrix like skin an onion, layer by layer and from outside to inside
              With 4 steps in loop and every time we start from (k,k), k is between in 0 and i_standard/2, which i_standard is determined by minimal of m and n
              (1)Top part:copy the range of k and n-k-1 elements in k-th array of the matrix
              (2)Right part: from top to down, copy the n-k-1 element in the arrays( (1+k)-th ~ (m-k-1) ) of the matrix
              (3)Bottom part:copy the range of k and n-k-1 elements in (m-k-1)-th array of the matrix, remember reverse the order before extend to the output array
              (4)Left part: from down to top, copy the k element in the arrays( (1+k)-th ~ (m-k-1) ) of the matrix
        """
        list_rtItem = []
        #If nothing in the matrix, just return the empty array
        if len(matrix) == 0:
            return list_rtItem
        #If one row only in the matrix, return the row
        if len(matrix) == 1:
            list_rtItem.extend(matrix[0])
        #If one column only in the matrix, copy all elements with the top-down order and return
        elif len(matrix[0]) == 1:
            for each_item in range(len(matrix)):
                list_rtItem.append(matrix[each_item][0])
        else:
            #Get the m and n, determine the i_standard
            i_rows = len(matrix)
            i_columns = len(matrix[0])
            i_standard = min(i_rows,i_columns)
            for each_layer in range(int(i_standard/2)):
                #Copy the Top part
                list_rtItem.extend(matrix[each_layer][each_layer:i_columns-each_layer])
                #Copy the Right part
                for each_row in range(1+each_layer,i_rows-1-each_layer):
                    list_rtItem.append(matrix[each_row][i_columns-each_layer-1])
                #Copy the Bottom part
                list_rtItem.extend(matrix[i_rows-1-each_layer][each_layer:i_columns-each_layer][::-1])
                #Copy the Left part
                for each_row in reversed(range(1+each_layer,i_rows-1-each_layer)):
                    list_rtItem.append(matrix[each_row][each_layer])
            
            #Exception handle - if single row/column remain after the loop ends
            if i_standard%2 == 1:
                i_center = int(i_standard/2)
                list_rtItem.extend(matrix[i_center][i_center:i_columns-i_center])
                if i_rows > i_columns:
                    for each_row in range(1+i_center,i_rows-i_center):
                        list_rtItem.append(matrix[each_row][i_columns-i_center-1])
                
        return list_rtItem