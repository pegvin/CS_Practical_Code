# Menu Driven program to work on a Binary file

import pickle

print("Tasks to be performed on Binary File..")
print("====================================")

print("1. Create new record")
print("2. Search records by Author Name")
print("3. Exit")

def CreateNewRecord():
	File = open("Book2.dat", "ab")
	BookRecords = []
	while True:
		book_no = int(input("Number: "))
		book_name = input("Book name: ")
		author_Name = input("Author name: ")
		price = float(input("Book cost: "))

		BookRecords.append([book_no, book_name, author_Name, price])

		ans = input("Want to add more records? ")
		if ans in ['n','N']:
			break

	pickle.dump(BookRecords, File)
	File.close()

def SearchRecord_ByAuthor(Author):
	File = open("Book2.dat", "rb")
	while True:
		try:
			BookRecords = pickle.load(File)
			for record in BookRecords:
				if record[2] == Author:
					print(record)
		except:
			break

	File.close()

while True:
	choice = int(input("Enter your choice: "))
	if choice == 1:
		CreateNewRecord()
	elif choice == 2:
		Author = input("Author name: ")
		SearchRecord_ByAuthor(Author)
	elif choice == 3:
		break

	ans = input("Another choice? ")
	if ans in ['n','N']:
		break

