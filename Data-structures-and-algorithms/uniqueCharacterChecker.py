def unique_character_checker(arr):
    arr = arr.replace(' ', '')
    characters = set()

    for ch in arr:
        if ch in characters:
            return False
        else:
            characters.add(ch)
    return True

if __name__ == "__main__":
    assert unique_character_checker("ad dsa ty") == False, "FAiled test case."
    assert unique_character_checker("ad sgh ty") == True, "FAiled test case."   
    "All test cases failed." 