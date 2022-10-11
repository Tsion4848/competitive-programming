class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        r = 0
        c = 0
        
        spiral = []
        
        while r < m and c < n:
            for i in range(c, n):
                spiral.append(matrix[r][i])
            r += 1
            for i in range(r, m):
                spiral.append(matrix[i][n-1])
            n -= 1
            if r < m:
                for i in range(n-1, c-1, -1):
                    spiral.append(matrix[m-1][i])
                m -= 1
            if c < n:
                for i in range(m-1, r-1, -1):
                    spiral.append(matrix[i][c])
                c += 1
        return spiral
