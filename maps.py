def depth_of_friends(my_dict,depth):
    '''
    given a depth, calculates the how many direct friends someone has. 
    If depth is 2 - you have to return the direct friends of the person plus the direct 
    friends of all of his direct friends.
    '''
    
    string_builder = ''
    key_iterator = iter(my_dict)
    for i in range(depth):
        try:
            current_key = next(key_iterator)  
            friends = my_dict[current_key]  
            for friend in friends:
                string_builder += friend + '\n' 
                if friend in my_dict.keys():
                    for j in my_dict[friend]:  
                        string_builder += j + '\n'     
        except StopIteration:
            break

    return string_builder.strip()

def number_of_friends_depth(mY_dict,depth)->int:
    counter=len(mY_dict[next(iter(mY_dict))])
    if depth==1:return counter
    key_iterator=iter(mY_dict)
    for i in range(1,depth):
        current_key=next(key_iterator)
        counter+=len(mY_dict[current_key])
    return counter
    
# print(number_of_friends_depth({'seb':['pat','ku','mariell'], 'pat':['felix', 'karl', 'marius']},2))

def calc_depth_times_scenarios(position, scenarios)->int:
    return [i*j for i in position for j in scenarios]


    