def common_elements(arr1, arr2):
    p1 = 0
    p2 = 0

    res = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1

        elif arr1[p1] > arr2[p2]:
            p2 += 1

        else:
            p1 += 1

    return res

if __name__ == "__main__":
    assert common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]) == [1,4,9], "Failed test case!"