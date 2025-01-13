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
        

sol = Solution()
print(sol.isPalindrome(121))