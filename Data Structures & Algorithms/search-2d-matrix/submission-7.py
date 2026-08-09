class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t_row = -1
        lt, rt = 0, len(matrix)-1
        while(lt < rt):
            md = (lt+rt)//2
            if matrix[md][0] == target:
                return True
            elif matrix[md][0] > target:
                if(md-1 >= 0):
                    rt = md-1
                else:
                    return False
            else:
                if(md+1 < len(matrix)):
                    if(matrix[md+1][0] > target):
                        print(f"t_row = {md}")
                        t_row = md
                        break
                    else:
                        lt = md+1
                else:
                    t_row = md
                    print(f"t_row = {t_row}")
                    break
        if(lt == rt):
            t_row = lt
        print(f"t_row = {t_row}")
        lt, rt, md = 0, len(matrix[t_row])-1, 0
        while(lt < rt):
            md = (lt+rt)//2
            if(matrix[t_row][md] == target):
                return True
            elif(matrix[t_row][md] > target):
                rt = md-1
            else:
                lt = md+1
        if(lt == rt):
            print(f"lt = {lt}, rt = {rt}")
            if(matrix[t_row][md] == target) or (matrix[t_row][lt] == target):
                return True
        return False
                