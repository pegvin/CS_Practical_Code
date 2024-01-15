# Menu Driven program to work on a csv file

import csv

print("Tasks to be performed on CSV File..")
print("====================================")

print("1. Create new record")
print("2. Display the record as per Roll no")
print("3. Exit")

def CreateFile():
	File = open("data3.csv", "w", newline="")
	Records = [] # Array Which Will Hold Records To Write
	writer = csv.writer(File, delimiter=",")
	writer.writerow(["adm No", "Name", "class", "Section", "Marks"])

	while True:
		adm_no = int(input("Adm. no: "))
		name = input("Name: ")
		grade = int(input("Class: "))
		section = input("Section: ")
		marks = float(input("Marks: "))

		Records.append([adm_no, name, grade, section, marks])

		ans = input("add 1 more record? ")
		if ans in ['n','N']:
			break

	for rec in Records: 
		writer.writerow(rec)

	File.close()

def DisplayRecord():
	File = open("data3.csv", "r")
	Records = csv.reader(File)
	for rec in Records:
		print(rec)

	File.close()

while True:
	choice = int(input("Enter your choice: "))
	if choice == 1:
		CreateFile()
	elif choice == 2:
		DisplayRecord()
	elif choice == 3:
		break

	ans = input("Another choice: ")
	if ans in ['n','N']:
		break

