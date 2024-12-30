def repeatingLetter(s:str, letter:str)->int:
    count=0
    for i in s:
        if i==letter: count+=1
    return count

def repeatingLetterFaster(s: str, letter: str) -> int:
    if len(letter) != 1 or not s:
        return 0
    return s.count(letter)

def iterString(s:str,letter:str)->int:
    iterator=iter(s)
    count=0
    while True:
        try:
            count+=(1 if next(iterator)==letter else 0)
        except StopIteration:
            break
    print(count)
    
    
