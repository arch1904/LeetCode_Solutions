class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in seen:
                j = seen[other_num]
                return [i, j]
            else:
                seen[nums[i]] = i
                
        return [-1, -1]

        