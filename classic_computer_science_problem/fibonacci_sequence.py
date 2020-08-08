from typing import Generator

def fibonacci(n: int) -> Generator[None, None, int]:
	yield 0
	if n > 1: yield 1
	last: int = 0
	next: int = 1
	for _ in range(1, n):
		last, next = next, last+next
		yield next


if __name__ == '__main__':
	for i in fibonacci(50):
		print (i)