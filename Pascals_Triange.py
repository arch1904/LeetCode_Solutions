'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30

'''
class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        res = [[1]]
        i = 1
        while i < numRows:
            res.append([])
            for j in range(0, i+1):
                if j == 0:
                    res[i].append(res[i-1][0])
                elif j == i:
                    k = len(res[i-1]) - 1
                    res[i].append(res[i-1][k])
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
            i += 1
        return res