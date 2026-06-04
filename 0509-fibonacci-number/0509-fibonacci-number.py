class Solution:
    def fib(self, n: int) -> int:
        #0 1 1 2 3 5 8
        if n==0:
            return 0
        if n==1:
            return 1
        a=0
        b=1
        i=2
        while i<=n:
            sum=a+b
            a=b
            b=sum
            i+=1
        return sum 