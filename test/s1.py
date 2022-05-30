import s2

"""
Program to attach salution to name with proper greetings...
"""
def fun1(name):
	# Choose salutation
	salute = s2.getSalutation(name)
	return "Hello, " + salute+" "+name

