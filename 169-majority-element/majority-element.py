class Solution:
    def majorityElement(self, nums):
        candidate, count = None, 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
