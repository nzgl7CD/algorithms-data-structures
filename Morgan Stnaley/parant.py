def legalParant(s:str)->bool:
    if not s: return False
    pointer=0
    valid='()'
    for i in s:
        if i in valid:
            pointer+=(1 if i=='(' else -1)
            if pointer<0: return False
    return True
