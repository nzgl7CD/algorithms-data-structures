#String
string="Algdat practice"
first_letter=string[0] # ->O(1)
slice_string=string[1:3] # -> O(k) also [start:stop:step]

new_string=string+" is fun" # -> O(n)
length=len(string) # -> O(1)

find_letter=string.find('Algdat') # -> O(m*n), where n=len(string) and m=len('Algdat')
is_in= 'A' in string # Bool output: -> O(n)

s='b'
order=ord(s) - ord('a') + 1 # return 2 as b is the second letter in the alphabet

orderlist=[ord(char.lower()) - ord('a') + 1 for char in s if char.isalpha()]

# print(ord('5')-ord('0'))

