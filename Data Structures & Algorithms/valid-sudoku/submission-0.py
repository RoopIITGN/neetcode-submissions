class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_d = [set() for _ in range(9)]
        c_d = [set() for _ in range(9)]
        b_d = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if(ele == '.'):
                    continue
                if ele in r_d[i] or ele in c_d[j] or ele in b_d[((i // 3) * 3) + (j // 3)]:
                    return False
                else:
                    r_d[i].add(ele)
                    c_d[j].add(ele)
                    b_d[((i // 3) * 3) + (j // 3)].add(ele)
        return True