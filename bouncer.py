age = input("How old are you?: ")
if age:
	age = int(age)
	if age >= 21:
		print("you can enter, but need a wristband")
	elif age >= 18:
		print("You good to enter and can drink!")
	else:
		print("You cant come in")
else:
	print("Please enter an age")

