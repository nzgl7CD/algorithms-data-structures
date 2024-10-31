def from_str_to_int(s:str)->int:
    is_negative=False
    start=0
    result=0
    if s[0]=='-':
        is_negative=True
        start=1
    for i in s[start:]:
        result=result*10+ord(i)-ord('0')
    return (~result+1 if is_negative else result) 
        
print(from_str_to_int('-455'))