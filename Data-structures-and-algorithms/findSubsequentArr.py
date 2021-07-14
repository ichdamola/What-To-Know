def subsequent_array_finder(arr1: list, arr2: list) -> bool:
    index_of_arr1_element, index_of_arr2_element = 0,0

    for x in range(len(arr2)):
        for y in range(len(arr1)):
            if arr2[x] == arr1[y]:
                index_of_arr1_element = index_of_arr2_element
                index_of_arr2_element = y
                if index_of_arr1_element > index_of_arr2_element:
                    return False
    return True


if __name__=="__main__":
    assert subsequent_array_finder([5,1,22,25,6,-1,8,10], [1,6,-1,10])==True, "Test failed"
    print("Passed all test cases!")

# TC: O(n*m), SC: O(1)