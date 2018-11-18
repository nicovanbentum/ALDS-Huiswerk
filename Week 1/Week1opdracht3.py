import time

"""
Function that calculates prime numbers up to n
VERY SLOW

Parameters
-------
max : integer
	range maximum you want to calculate for

Return
-----
filledList : list
	contains all the prime numbers found

"""
def findPrimes(max):
	filledList = []
	for i in range(2, max):
		filledList.append(i)

	for nr in filledList:
		for marked_nr in range(nr*nr, max, nr):
			try:
				filledList.remove(marked_nr)
			except ValueError:
				pass #passing the ValueError costs less than "if nr in filledList"
	return filledList

"""
Function that calculates prime numbers up to n
VERY FAST
huge memory footprint though

Parameters
-------
max : integer
	range maximum you want to calculate for

Return
-----
returnList : list
	contains all the prime numbers found

"""
def findPrimesBoolean(max): #very fast
	filledList = []
	booleanList = []
	returnList = []

	for i in range(2, max):
		filledList.append(i)
		booleanList.append(True)

	n = len(filledList)

	for nr in filledList:
		for marked_nr in range(nr*nr, max, nr):
			booleanList[marked_nr-2] = False

	for i in range(0, n):
		if booleanList[i] == True:
			returnList.append(i+2)

	return returnList

#simple tests
m = 40000

start = time.time()
findPrimes(m) #doesn't flood console, wrap in print() to output the actual prime numbers
end = time.time()
print("Find primes time where max = " + str(m) + " : " + str(end-start) + " seconds.")

start = time.time()
findPrimesBoolean(m) #10'000'000
end = time.time()
print("Find primes BOOLEAN time where max = " + str(m) + " : " + str(end-start) + " seconds.")