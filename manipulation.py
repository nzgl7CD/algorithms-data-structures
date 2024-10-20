def nextGreatest(num:int)->int:
    '''
    Manipulate integers 
    '''
    numDivided=[int(i) for i in str(num)]
    firstDigit,next_num=numDivided.pop(0),0
    numDivided.sort()
    for i in range(len(numDivided)):
        if numDivided[i]>firstDigit:
            next_num=firstDigit
            firstDigit=numDivided.pop(i)
            break
    return int(str(firstDigit)+str(next_num)+''.join(str(no) for no in numDivided))
# print(nextGreatest(4765))

def reverseString(s:str)->str:
    return ' '.join(list(word for word in s.split()[-1::-1]))


