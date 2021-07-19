def pair_sum(arr, target):
    seen = set()
    res = set()

    if len(arr) < 2:
        return ()

    for num in arr:
        summingPair = target - num

        if summingPair not in seen:
            seen.add(num)
        else:
            res.add((min(num, summingPair), max(num, summingPair)))
    return res


print(pair_sum([1,3,2,2], 4))

if __name__ == "__main__":
    assert pair_sum([1,3,2,2], 4) == {(1,3),(2,2)}, "Test case failed"
    "ALl test cases failed!"