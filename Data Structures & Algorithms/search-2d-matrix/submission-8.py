class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1

        t = 0
        b = len(matrix)-1

        while t <= b:
            m = (t+b)//2
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[m])-1]:
                while l <= r:
                    mm = (l+r)//2
                    if target == matrix[m][mm]:
                        return True
                    elif target < matrix[m][mm]:
                        r = mm-1
                    else:
                        l = mm+1
                return False
            elif target < matrix[m][0]:
                b = m-1
            else:
                t = m+1
        return False