# Menu Driven program to work on a Stack

print("Tasks to be performed on Stack..")
print("====================================")

print("1. Push")
print("2. Pop")
print("3. Traverse")
print("4. Exit")

Stack = []

def Push():
	e_no = int(input("Employee number: "))
	e_name = input("Employee name: ")
	e_salary = float(input("Employee salary: "))     
	Stack.append([e_no, e_name, e_salary])

def Pop():
	if len(Stack) == 0:
		print("Stack is empty")
	else:
		element = Stack.pop()
		print("Element deleted from the stack..>", element)

def traverse():
	if len(Stack) == 0:
		print("Stack is empty")
	else:
		for i in range(len(Stack), 0, -1): # Run a For Loop from `len(Stack)` to Zero By Subtracting `-1`, i.e. in Reverse
			print("---->", Stack[i - 1])

while True:
	choice = int(input("Enter your choice: "))
	if choice == 1:
		Push()
	elif choice == 2:
		Pop()
	elif choice == 3:
		traverse()
	elif choice == 4:
		break

	ans = input("Another choice: ")
	if ans in ['n','N']:
		break

