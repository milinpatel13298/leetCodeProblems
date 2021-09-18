class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer=[]
        while matrix:
            #first row
            answer.extend(matrix[0])
            matrix=matrix[1:][:]
            
            if not matrix:
                break
            
            #last column
            answer.extend([matrix[i][len(matrix[0])-1] for i in range(len(matrix))])
            for i in range(len(matrix)):
                matrix[i]=matrix[i][:-1]
                
            if not matrix:
                break
                
            #last row reversed
            reversedLastRow=matrix[-1]
            reversedLastRow.reverse()
            answer.extend(reversedLastRow)
            matrix=matrix[:-1][:]
            
            if not matrix:
                break

            #first column reversed
            answer.extend([matrix[i][0] for i in range(len(matrix)-1,-1,-1)])
            for i in range(len(matrix)):
                matrix[i]=matrix[i][1:]
            
        return answer
