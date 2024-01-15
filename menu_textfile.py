# Menu Driven program to work on a text file

print("Tasks to be performed on Text File..")
print("====================================")

print("1. Create a file")
print("2. Display File content ")
print("3. Display the number of Lines starting with 'I'")
print("4. Display Average length of words")
print("5. Exit")

def create_file():
	File = open("text.txt", "a")
	File.write("India is my Country\n")
	File.write("I love my country\n")
	File.write("I am proud of my country\n")
	File.write("It has rich and varied heritage\n")
	File.close()

def display_file():
	File = open("text.txt", "r")
	Contents = File.read()
	print("The file content is...")
	print(Contents)
	File.close()

def count_line():
	count = 0
	File = open("text.txt", "r")
	Lines = File.readlines()

	for Line in Lines:
		if Line[0] == "I":
			count += 1

	print("The number of lines starting with I are", count)
	File.close()

def avg_word_l():
	NumLetters = 0
	NumWords = 0
	File = open("text.txt", "r")
	Contents = File.read()
	words = Contents.split()

	for word in words:
		NumLetters += len(word)
		NumWords += 1

	AverageLength = NumLetters / NumWords
	print("The average number of words are", AverageLength)
	File.close()

while True:
	choice = int(input("Enter your choice: "))
	if choice == 1:
		create_file()
	elif choice == 2:
		display_file()
	elif choice == 3:
		count_line()
	elif choice == 4:
		avg_word_l()
	elif choice == 5:
		break

	ans = input("Another choice? ")
	if ans in ['n','N']:
		break

