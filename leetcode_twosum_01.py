class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 
        
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in seen:
                return [seen[rest], i]
            seen[nums[i]] = i
        
        return []

print(Solution().twoSum([2,7,11,15],9))