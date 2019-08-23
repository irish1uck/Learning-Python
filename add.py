def add(x):
	y = input("What do you want to add?")
	y = str(y)
	while len(y) > 0:
		x.append(y)
		y = input("Anything else?")
		y = str(y)
		if len(y) <= 0:
			print("Done!")
