
"""
Function that returns any numbers it finds in a given string

Parameters
-------
s : string
	string to parse

Return
-----
returnList : list
	list containing all numbers found

"""
def getNumbers(s):
	returnList = []
	list_string = ""

	for character in s:
		if character.isdigit():
			list_string = list_string + character
		else:
			if list_string != "":
				returnList.append(list_string)
				list_string = ""

	return returnList



myString = "een123zin45 6met-632meerdere+777getallen"
print(getNumbers(myString))