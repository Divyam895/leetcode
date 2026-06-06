class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=0
        for i in range(0,len(nums)):
            if n!=nums[i]:
                return n
            n+=1
        return n