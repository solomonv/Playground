from fortune import fortune

def menu():
	query = raw_input("What would you like to run?\n1. Magic Eight Ball ")
	if len(query) > 0 and query != query.isalpha():
		if query == "1":
			print "running Magic Eight Ball\n"
			fortune()
		else:
			"That is not an option"
	else:
		"Not a valid option"

menu()