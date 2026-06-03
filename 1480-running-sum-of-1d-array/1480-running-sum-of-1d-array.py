class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls=[]
        for i in range(0,len(nums)):
            if i==0:
                ls.append(nums[i])
            else:
                ls.append(nums[i]+ls[i-1])
        return ls
