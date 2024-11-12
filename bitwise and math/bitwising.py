def count_set_bits(num):
    counter=0
    while num:
        if num&1: counter+=1
        num>>=1
    return counter
# print(count_set_bits(10))

def is_odd(num:int)->bool:
    return num&1==1

def convert_from_string_to_bin(stri:str)->int:
    return int(stri[2:],2)

def frombintoint(binstring:str):
    if binstring[1]=='b':
        return int(binstring[2:],2)
    return int(binstring,2)

def half_to(num:int)->int:
    return num>>3
# print(half_to(16))

def make_pair(num:int)->int:
    return ((num+1)&~1 if num&1==1 else num)
# print(make_pair(1))

def findPrime(num:int):
    dividers=[i for i in range(2,int(num**0.5)+1)]
    sqrt=int(num**0.5+1)
    return not any(num%i==0 for i in range(2,sqrt)) 
# print(findPrime(7))

def only_pairs(arr:list[int]):
    return set(filter(lambda x: not x&1, arr))


def make_pairs(arr:list[int]):
    return list(x & ~1 for x in arr)

# print(make_pairs([1,2,3,4,7]))

def is_prime(num):
    if not num or num<=2: return
    sqroot=int(num**0.5+1)
    starter=(3 if num&1==1 else 2)
    return not any(num%i==0 for i in range(starter,sqroot,2))
# print(is_prime(3))

def sum_ints(a:int,b:int):
    while b:
        sum_without_carry = a ^ b
        carry = (a & b) << 1
        a = sum_without_carry
        b = carry
        
    return a
        
a=10 # 1010
b=3 # 0011



