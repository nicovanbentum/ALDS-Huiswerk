"""
Function that returns the biggest integer in a list

Parameters
-------
a : list
	list to check for biggest integer

Return
-----
biggestNumber : integer
	represents the biggest integer found
	
"""
def myMax(a):
	if len(a) == 0:
		return

	biggestNumber = myList[0]

	for item in myList:
		assert type(item) is int, "fail"

		if item > biggestNumber:
			biggestNumber = item
	return biggestNumber

myList = [5, 10, 5, 41, 77, 13, 2]
print(str(myMax(myList)))
	