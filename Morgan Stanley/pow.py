class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        elif n<0: return 1/self.myPow(x,-n)
        elif n&1==1: return x*self.myPow(x,n-1)
        else: half_pow=self.myPow(x,n>>1); return half_pow*half_pow
print(Solution().myPow(2,4)) 