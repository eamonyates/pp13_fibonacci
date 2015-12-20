def fibonacci ():
	user_num = int(input("How many numbers of the fibonacci sequence would you like to see: "))
	x = 0
	fibonacci_list = []
	while x < user_num:
		x += 1
		if len(fibonacci_list) <= 1:
			fibonacci_list.append(1)
		else:
			fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
	print (fibonacci_list)


if __name__ == "__main__":
	fibonacci()
