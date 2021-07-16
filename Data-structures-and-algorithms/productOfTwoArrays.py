'''
def array_of_array_products(arr):
  lengthArr = len(arr)
  output = []
  
  for i in range(len(arr)):
    multi = 1
    for j in range(len(arr)):
      if j == i:
        continue
      else:
        multi *= arr[j]
    output.append(multi)
    multi = 1
    j = i + 1
    
  return output
'''

def array_of_array_products(arr):
  lengthArr = len(arr)
  res = [1] * lengthArr

  prefix = 1
  for i in range(lengthArr):
    res[i] = prefix
    prefix *= arr[i]

  postfix = 1
  for i in range(lengthArr-1, -1, -1):
    res[i] *= postfix
    postfix *= arr[i]

  return res


if __name__ == "__main__":
  assert (array_of_array_products([8,10,2]))==[20,16,80], "Failed test."
  print("All test cases passed!")

# arr = [8, 10, 2]
# arr1 = [2, 7, 3, 4]
# print(array_of_array_products(arr1))
