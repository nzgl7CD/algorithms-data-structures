def iterate_dicts(s="23"):
    digit_to_letters = {'2': 'abc', '3': 'def', '4': 'ghi'}
    combos = []

    for i in range(len(s)):
        digit1 = s[i]
        letters1 = digit_to_letters[digit1]
        
        for j in range(i+1,len(s)):
            digit2 = s[j]
            letters2 = digit_to_letters[digit2]

            for l in letters1:
                for z in letters2:
                    combos.append(l + z)

    return combos

iterate_dicts("23")