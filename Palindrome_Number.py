'''
9. Palindrome Number

Given an integer x, return true if x is a
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # Sol with String
        # num_str =  str(x)
        # print(num_str[:: -1])
        # if num_str == num_str[:: -1]:
        #     return True
        # return False

        div = 1
        while x >= 10 * div:
            div *= 10
        print (div)
        while x != 0:
            l = x % 10
            r = x // div

            if l != r:
                return False
            x = (x % div) // 10
            print(x)
            div /= 100
        return True
        