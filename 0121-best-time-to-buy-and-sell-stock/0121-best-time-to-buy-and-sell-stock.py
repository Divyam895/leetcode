class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        prof=0
        for i in prices:
            if min>i:
                min=i
            prof=max(prof,i-min)
        return prof
