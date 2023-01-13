name =input("What's your name? ") 

match name:
	case "Harry" | "Hermonie" | "Ron":
		print("Griffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")