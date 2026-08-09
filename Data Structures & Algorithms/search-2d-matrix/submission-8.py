class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        lt, rt = 0, len(matrix)-1
        while(lt <= rt):
            md = (lt+rt)//2
            if(matrix[md][0] > target):
                rt = md-1
            elif(matrix[md][-1] < target):
                lt = md+1
            else:
                break
        if(lt > rt):
            return False
        row = (lt+rt)//2
        lt, rt = 0, len(matrix[0])
        while(lt <= rt):
            md = (lt+rt)//2
            if(matrix[row][md] > target):
                rt = md-1
            elif(matrix[row][md] < target):
                lt = md+1
            else:
                return True
        
        return False
                