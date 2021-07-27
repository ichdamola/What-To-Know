"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""
def longestConsecutive(nums) -> int:
    nums.sort()
    max_element = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < max_element:
            max_element = nums[i]
                
    for i in range(len(nums)):
        if nums[i] == max_element + 1:
            max_element = nums[i]
                
    return max_element


if __name__ == "__main__":
    assert longestConsecutive([100,4,200,1,3,2]) == 4, "Failed test cases."