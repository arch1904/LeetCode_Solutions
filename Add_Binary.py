'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.

'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = len(a) - len(b)
        if diff < 0:
            for i in range(abs(diff)):
                a = '0' + a
        elif diff > 0:
            for i in range(diff):
                b = '0' + b
        i = len(a) - 1
        return self.addBinRecur(a, b, '0', '', i)
    
    def addBinRecur(self, a, b, r, res, i):
        if i < 0:
            if r == '1':
                res = r + res
            return res
        if a[i] == '1' and b[i] == '1':
            if r == '0':
                res = '0' + res
                return self.addBinRecur(a,b,'1',res, i -1)
            elif r == '1':
                res = "1" + res
                return self.addBinRecur(a, b, '1', res, i - 1)

        elif (a[i] == '0' and b[i] == '1') or (a[i] == '1' and b[i] == '0'):
            if r == '0':
                res = '1' + res
                return self.addBinRecur(a, b, '0', res, i - 1)
            elif r == '1':
                res = '0' + res
                return self.addBinRecur(a, b, '1', res, i - 1)
        elif a[i] == '0' and b[i] == '0':
            if r == '0':
                res = '0' + res
            else:
                res = "1" + res
            return self.addBinRecur(a, b, '0', res, i - 1)