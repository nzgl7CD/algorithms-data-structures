class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz',}
        for i in m: m[i]=list(m[i])
        self.ans=[]
        def foo(idx,curr): # 
            if idx==len(digits): 
                self.ans.append(curr)
                return
            for letter in m[digits[idx]]: foo(idx+1,curr+letter)
        foo(0,"")
        return filter(lambda x:len(x)>0, self.ans)

for i in Solution().letterCombinations('23'):
    print(i)