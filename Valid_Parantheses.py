'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'(':')', '[':']', '{':'}'}
        open_chars = matching.keys()
        close_chars = matching.values()
        for c in s:
            if c in open_chars:
                stack.append(c)
            elif c in close_chars:
                if not stack:
                    return False
                x = stack.pop()
                if matching[x] != c:
                    return False
        return not stack