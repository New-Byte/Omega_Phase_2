list_ = ["i","a","y","u","e","o"]

def getSalutation(name):
	''' if name ends with letter in list_
	it is most likely to be the girl's name'''

	# Get salutations for the input name
	if name[-1] not in list_:
		return "Mr."
	else:
		return "Miss"