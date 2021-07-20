def get_different_number(arr):
  
  arr.sort()
  n = len(arr)
  for i in range(n):
    if arr[i] != i:
      return i
  return n

print(get_different_number([1,0, 2, 3]))