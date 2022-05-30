import random

# Set new color each time app is launched
def getColor():
	return "#"+str(int(str(random.randint(1118481,16777215)),16))[:6]