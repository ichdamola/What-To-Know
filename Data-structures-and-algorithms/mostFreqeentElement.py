def most_frequent(arr):
    elements = {}
    max_count = 0
    max_element = None

    for element in arr:
        if element not in elements:
            elements[element] = 1
        else:
            elements[element] += 1

        if elements[element] > max_count:
            max_count = elements[element]
            max_element = element

    return max_element

if __name__ == "__main__":
    assert most_frequent([1,1,1,1,2,2,3,1,4,5]) == 1, "Test case failed!"
    assert most_frequent([1,3,3,3,3,3,1,2,2,3,1,4,5]) == 3, "Test case failed!"
    "Failed all test cases!"
