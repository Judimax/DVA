class Array:
	def __init__(self, parm1):
		self.innerlist = []
		if type(parm1) == list:
			self.size = len(parm1)
			for x in parm1:
				self.innerlist.append(x)
		else:
			self.size = parm1
			for i in range(self.size):
				self.innerlist.append(None)

	def __str__(self):
                return str(self.innerlist)
	
                                                              
	
	def __getitem__(self, index):
		if index >= 0 and index < self.size:
			return self.innerlist[index]
		else:
			raise ValueError("Array index out of bounds")

	def __setitem__(self, index, newvalue):
		if index >= 0 and index < self.size:
			self.innerlist[index] = newvalue
		else:
			raise ValueError("Array index out of bounds")

	def __len__(self):
		return self.size

	#def getlist(self):
	#	return self.innerlist

	def __list__(self):
		return self.innerlist

	def __iter__(self):
		self.__i__ = 0
		return self

	def __next__(self):
		if self.__i__ < self.size:
			k = self.__i__
			self.__i__ += 1
			return self.innerlist[k]
		else:
			raise StopIteration
		

def main():
	heat = Array(10)   # fixed size array, cannot go outside bounds
	heat[0] = 75
	heat[1] = 55
	heat[2] = 97
	print(heat[1])
	#heat[20] = 55
	stuff = Array([57,26,33,97])   # start out with these values, also size is fixed to 4
	print(stuff[3])
	print("  now iterate  ")
	for k in stuff:
		print("----",k)
	z = list(stuff)
	print(z)
	#stuff[4] = 999    # or comment this out and proceed to the following

	try:
		stuff[4] = 999
	except ValueError:
		print("Illegal array operation")

if __name__ == "__main__":
	main()
