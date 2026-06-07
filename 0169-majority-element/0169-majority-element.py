class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
                if c[i]>(len(nums)/2):
                    return i
            else:
                c[i]=1
                if c[i]>(len(nums)/2):
                    return i