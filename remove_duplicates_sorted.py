def remove_duplicates(nums: list[int]) -> int:
    insert_index = 1
    for idx, ele in enumerate(nums[1:], 1):
        if ele != nums[idx - 1]:
            nums[insert_index] = ele
            insert_index += 1
    return insert_index

if __name__ == "__main__":
    assert remove_duplicates([1,1,2]) == 2
    assert remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5
