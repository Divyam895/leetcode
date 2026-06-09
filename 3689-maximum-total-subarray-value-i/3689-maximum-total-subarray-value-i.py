class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nums.sort()
        return k*(max(nums)-min(nums))