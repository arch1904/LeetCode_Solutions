'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        time_saver = {}
        return self.stairRecur(n, time_saver)
    
    def stairRecur(self, n, time_saver):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if (n - 1) in time_saver.keys() and (n - 2) in time_saver.keys():
                return time_saver[n -1] + time_saver [n - 2]
            elif (n -1) in time_saver.keys():
                time_saver [ n - 2] = self.stairRecur(n - 2, time_saver)
            elif (n - 2) in time_saver.keys():
                time_saver[n - 1] = self.stairRecur( n - 1 , time_saver)
            else:
                time_saver[n - 1] = self.stairRecur(n - 1 , time_saver)
                time_saver [n - 2] = self.stairRecur(n - 2 , time_saver)
            return time_saver[n - 1] + time_saver [ n - 2]

sol = Solution()
print(sol.climbStairs(100))