def min_sum(nums1: list[int], nums2: list[int]) -> int:
    num_zeros_one, num_zeros_two = (
        len([x for x in nums1 if x == 0]),
        len([x for x in nums2 if x == 0]),
    )
    sum1, sum2 = (
        sum(nums1) + num_zeros_one,
        sum(nums2) + num_zeros_two,
    )
    if (num_zeros_one == 0 and sum2 - sum1 > 0) or (
        num_zeros_two == 0 and sum1 - sum2 > 0
    ):
        return -1
    return max(sum1, sum2)


if __name__ == "__main__":
    assert min_sum([3, 2, 0, 1, 0], [6, 5, 0]) == 12
    assert min_sum([2, 0, 2, 0], [1, 4]) == -1
