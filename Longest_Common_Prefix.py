'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lowest_length_string = "1" * 202
        for s in strs:
            if len(s) < len(lowest_length_string):
                lowest_length_str = s
        for i in range(len(lowest_length_string), -1, -1):
            check_str = lowest_length_str[:i]
            if check_str == '':
                return check_str
            flag = False
            l = len(check_str)
            for j in range(len(strs)):
                if check_str !=  strs[j][:l]:
                    flag = False
                    break
                else:
                    flag = True
            if flag == True:
                return check_str
