def rizzbuzz():
	for x in range(1, 101):
		if x % 3 == 0 and x % 5 == 0:
			print("Rizz Buzz!")
		elif x % 3 == 0:
			print("Rizz!")
		elif x % 5 == 0:
			print("Buzz!")
		else:
			print(x)
