# pass
def bestGreed(arr:list[int])->int:
    if not arr: return 0 
    min_price=float('inf')
    max_profit=0
    for i in arr:
        if i<min_price:
            min_price=i
        max_profit=max(max_profit,i-min_price)
    return max_profit
# print(bestGreed([2,3,-1,5,4,9]))

# pass
def twoSum(arr:list[int], target:int)-> list[int]:
    if not arr: return
    dict={}
    for idx, num in enumerate(arr):
        temp=target-num
        if temp in dict:
            return [dict[temp], idx]
        dict[num]=idx
    return []

def getIntersectionNode(headA, headB):
    if not headA and not headB: return None
    ptrA, ptrB=headA, headB
    while ptrA!=ptrB:
        ptrA=ptrA.next if ptrA else headB
        ptrB=ptrB.next if ptrB else headA
    return ptrA

def reverse_list(head):
    if head is None or head.next is None:
        return head
    rest = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return rest
    
#pass
def maxSubArray(nums: list[int]) -> int:
    if not nums: return 0
    current_max=nums[0]
    final_max=nums[0]
    for i in nums[1:]:
        current_max=max(current_max,current_max+i)
        final_max=max(final_max,current_max)
    return final_max
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))

# Almost -> add fifo
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self._catch={}
        self.prev=[]

    def get(self, key: int) -> int:
        try:
            return self._catch[key]
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self._catch)>=self.capacity:
            del self._catch[self.prev.pop(0)]
        self.prev.append(key)
        self._catch[key]=value

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# lRUCache.put(3, 3)
# print(lRUCache.get(2))

#passed
def valid_anagram(s:str, t:str)->bool:
    return sorted(s)==sorted(t)

#Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
def firstMissingPositive(nums: list[int]) -> int:
    n=len(nums)
    i=0
    while i<n:
        num_at_i=nums[i]-1
        belongs_in_range=0<=num_at_i<n
        
        if belongs_in_range and nums[i]!=nums[num_at_i]:
            nums[i], nums[num_at_i]=nums[num_at_i], nums[i]
        else:
            i+=1
            
    for x in range(n):
        if x+1!=nums[x]:
            return x+1
    return n+1

def myPow(x,n):
    if n==0:
        return 1
    elif n<0:
        return 1/myPow(x,n)
    elif n&1==0:
        half_power=myPow(x,n//2)
        return half_power * half_power
    else:
        return x * myPow(x,n-1)
print(myPow(2,10))

def minCostToMoveChips(position: list[int]) -> int:
    odds,pairs=0,0
    for i in position:
        if i&1==1:
            odds+=1
        else:
            pairs+=1
    return min(odds, pairs)

# print linked list
def print_list(node):
    while node is not None:
        print(f" {node.data} ->", end='')
        node = node.next
    print()

# Partly passed
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
    
# obj=MinStack()
# obj.push(10)
# obj.push(5)
# obj.push(2)
# print(obj.top())
# print(obj.getMin())
    


        
