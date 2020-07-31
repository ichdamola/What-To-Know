def fibonacci(n: int) -> int:
	if n < 2: # base case
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
	print(fibonacci(4))
	# print (fibonacci(49)) Dont call