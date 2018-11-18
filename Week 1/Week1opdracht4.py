import time
from secrets import randbelow

"""
Bubble sorts any given list

Parameters
-------
lst : list
	the list you want sorted

Return
-----
void

"""
def bubblesort(lst):
	n = len(lst)

	for i in range(0, n-1):

		swapped = False

		for j in range(0, n-i-1):

			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
				swapped = True

		if swapped == False:
			break


"""
Checks if a list contains a pair, list has to be sorted

Parameters
-------
lst : list
	list you want to check

Return
-----
Boolean
	If it finds a pair returns True, if not returns False

"""
def foundPair(lst):
	n = len(lst)

	for i in range(0, n-1):
		if lst[i] != lst[i+1]:
			continue
		else:
			return True
			
	return False

"""
Function that calculates the odds n amount of students in n size class share a birthday,
assuming every class contains the same amount of students.

Parameters
-------
students : integer
	amount of students
classes : integer
	amount of classes

Return
-----
pair_count/classes : float
	floating value that represents the odds

"""
def calc_odds_list(students, classes): 
	list_lists = [] #contains lists 
	list_to_append = [] #contains random integers between 1 and 365

	for _ in range(classes):
		list_to_append = []
		for _ in range(students):
			random_int = randbelow(365)
			list_to_append.append(random_int)
		list_lists.append(list_to_append)

	pair_count = 0
	for lst in list_lists:
		bubblesort(lst)
		if foundPair(lst):
			pair_count += 1

	return pair_count/classes #varying results every time you run this function

"""
Function that calculates the odds n amount of students share a birthday.

Parameters
-------
students : integer
	amount of students

Return
-----
p : float
	floating value that represents the odds

"""
def calc_odds_math(students):
	a = 365
	b = 365

	for i in range(1, students):
		a = a * (365-i) #very big integer(s), can be a problem
		b = b * 365		

	p = 1 - (a/b)
	return p

#output tests
print(calc_odds_list(23, 100)) #should be around 0.50, 50% chance

start = time.time()
print(calc_odds_list(57, 100)) # around 0.99, 99% chance
end = time.time()
print("List function elapsed time: " + str(end-start) + " seconds.")

print(calc_odds_math(23))

start = time.time()
print(calc_odds_math(57))
end = time.time()
print("Pure math function elapsed time: " + str(end-start) + " seconds.")