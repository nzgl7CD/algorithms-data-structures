def from_str_to_int(s:str)->int:
    is_negative=1
    start=0
    result=0
    if s[0]=='-':
        is_negative=-1
        start=1
    for i in s[start:]:
        result=result*10+(ord(i)-ord('0'))
        
    return is_negative*result
        
print(from_str_to_int('-455'))