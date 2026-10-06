class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #space of ologn, sorting algo stack space
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue #we skip the term without adding to time complex drastically
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                if total < 0:
                    l += 1
                if total == 0:
                    #if [nums[i], nums[l], nums[r]] not in result:
                    result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result
        
        