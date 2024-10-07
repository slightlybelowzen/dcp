def kadane_no_wrap(nums: list[int]) -> int:
    max_so_far = max_subarray_sum = 0
    for num in nums:
        max_so_far = max(num, num + max_so_far)
        max_subarray_sum = max(max_subarray_sum, max_so_far)
    return max_subarray_sum


if __name__ == "__main__":
    assert kadane_no_wrap([34, -50, 42, 14, -5, 86]) == 137
