def remove_element(nums: list[int], val: int) -> int:
    insertion_index = 0
    for ele in nums:
        if ele != val:
            nums[insertion_index] = ele
            insertion_index += 1
    return insertion_index

if __name__ == "__main__":
    assert remove_element([3,2,2,3], 2) == 2
    assert remove_element([0,1,2,2,3,0,4,2], 2) == 5 
