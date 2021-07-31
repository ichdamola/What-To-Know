"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""
def longestConsecutive(nums) -> int:

    if len(nums) == 0:
        return 0
    
    numSet = set(nums)

    result = 0
    for num in nums:
        counter = 1
        if num-1 not in numSet:
            while num+1 in numSet:
                num += 1
                counter += 1
            result = max(result, counter)
    return result


if __name__ == "__main__":
    assert longestConsecutive([100,4,200,1,3,2]) == 4, "Failed test cases."