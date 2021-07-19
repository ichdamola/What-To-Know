def array_rotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    key = arr1[0]
    key_index = 0

    for i in range(len(arr2)):
        if arr2[i] == key:
            key_index = i

            break
    if key_index == 0:
        return False

    for j in range(len(arr1)):
        arr2_index = (key_index + j) % len(arr1)

        if arr1[j] != arr2[arr2_index]:
            return False
            
    return True

# Test
if __name__ == "__main__":
    assert array_rotation([1,2,3,4,5,6,7], [5,6,7,1,2,3,4]) == True, "Test case failed"