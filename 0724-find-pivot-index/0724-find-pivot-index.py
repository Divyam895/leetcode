class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=0
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        for i in range(0,len(nums)):
            lsum=sum(nums[0:i])
            rsum=sum(nums[i+1:])
            if lsum==rsum:
                return i
        return -1 