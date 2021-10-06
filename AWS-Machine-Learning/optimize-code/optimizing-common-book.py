import time
import pandas as pd
import numpy as np

with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')

with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

## Tip #1: Use vector operations over loops when possible

start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

## Tip #2: Know your data structures and which methods are faster

start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

