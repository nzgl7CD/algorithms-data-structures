import collections
def is_anagram(a:str,b:str)->bool:
    if not a or not b: return False
    return sorted(a)==sorted(b)

def is_anagram_II(a:str,b:str)->bool:
    count=collections.defaultdict(int)
    for i in a:
        count[i]+=1
    for j in b:
        count[j]-=1
    for x in count.values():
        if x!=0: return False
    return True

# print(is_anagram_II('aabc','cbaa'))

def sort_anagrams(words:list[str]):
    if not words: return []
    
    sort_words={}
    for word in words:
        temp_word=''.join(sorted(word))
        if temp_word not in sort_words: sort_words[temp_word]=[word]
        else: sort_words[temp_word].append(word)
    return sort_words



def new_anagram_sorter(words:list[str]):
    if not words: return
    sorter={}
    for word in words:
        keyWord=''.join(sorted(word))
        if keyWord in sorter: sorter[keyWord].append(word)
        else: sorter[keyWord]=[word]
    return sorter
print(new_anagram_sorter(['text','xett','ttex','abc','cbc','cba']))

def anagramUsingCollections(words:list[str]):
    if not words: return 
    defDict=collections.Counter()
    for i in words:
        defDict.update(sorted(i))
    return defDict.most_common(1)[0][1]
print(anagramUsingCollections(['text','xett','ttex','abc','cbc','cba']))

