# Disjoint set data structure
# Find whether x and y belong to the same group or not, i.e. to find if x and y are direct/indirect friends.

'''
Array: An array of integers is called Parent[]. If we are dealing with N items, i'th element of the array represents the i'th item. 
More precisely, the i'th element of the Parent[] array is the parent of the i'th item. These relationships create one or more virtual trees.
'''

class DisjSet: 
	def __init__(self, n): 
		# Constructor to create and 
		# initialize sets of n items 
		self.rank = [1] * n 
		self.parent = [i for i in range(n)] 


	# Finds set of given item x 
	def find(self, x): 
		
		# Finds the representative of the set 
		# that x is an element of 
		if (self.parent[x] != x): 
			
			# if x is not the parent of itself 
			# Then x is not the representative of 
			# its set, 
			self.parent[x] = self.find(self.parent[x]) 
			
			# so we recursively call Find on its parent 
			# and move i's node directly under the 
			# representative of this set 

		return self.parent[x] 


	# Do union of two sets represented 
	# by x and y. 
	def Union(self, x, y): 
		
		# Find current sets of x and y 
		xset = self.find(x) 
		yset = self.find(y) 

		# If they are already in same set 
		if xset == yset: 
			return

		# Put smaller ranked item under 
		# bigger ranked item if ranks are 
		# different 
		if self.rank[xset] < self.rank[yset]: 
			self.parent[xset] = yset 

		elif self.rank[xset] > self.rank[yset]: 
			self.parent[yset] = xset 

		# If ranks are same, then move y under 
		# x (doesn't matter which one goes where) 
		# and increment rank of x's tree 
		else: 
			self.parent[yset] = xset 
			self.rank[xset] = self.rank[xset] + 1

# Driver code 
obj = DisjSet(5) 
obj.Union(0, 2) 
obj.Union(4, 2) 
obj.Union(3, 1) 
if obj.find(4) == obj.find(0): 
	print('Yes') 
else: 
	print('No') 
if obj.find(1) == obj.find(0): 
	print('Yes') 
else: 
	print('No') 

# This code is contributed by ng24_7. 
