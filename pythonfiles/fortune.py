
from sols_utils import choose

def fortune():
	run = True
	print "\n---Magic Eight Ball---\n"
	print "type 'x' to exit\n"
	while run == True:
		question = raw_input("What do you ask? ").lower()
		answers = ["Most assuredly", "That does not seem wise.", "Follow your heart.", "If it tastes good!", "Probably not.", "What would your mother say?", "Yes!", "No!"]
		if question != 'x':
			print "---------\n" + choose(answers) + "\n"
		else:
			run = False
			print("May the force be with you.")
if __name__ == "__main__":
	fortune()
