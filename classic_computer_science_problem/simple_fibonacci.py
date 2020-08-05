def fibonacci(n: int) -> int:
	if n < 2: return n
	last: int=0
	next: int=1
	for _ in range(1, n):
		last, next = next, last + next
	return next

if __name__ == "__main__":
	print(fibonacci(50))

# def fib5(n: int) -> int:
# 	if n < 2: return n # special case
# 	last: int= 0 # initially set to fib(0)
# 	next: int= 1 # initially set to fib(1)
# 	for _ in range(1, n):
# 		last, next = next, last + next
# 	return next

# if __name__ == "__main__":
# 	print(fib5(5))
# 	print(fib5(50))