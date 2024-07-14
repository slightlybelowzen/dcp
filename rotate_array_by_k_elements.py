def solve(nums: list[int], k: int) -> list[int]:
    # this is the less memory efficient way with copies of the array
    # return nums[k:] + nums[0:k]

    # is this really better?
    nums.reverse()
    length = len(nums)
    nums[: length - k] = nums[: length - k][::-1]
    nums[length - k :] = nums[length - k :][::-1]
    return nums


if __name__ == "__main__":
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=1) == [2, 3, 4, 5, 6, 1]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=2) == [3, 4, 5, 6, 1, 2]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=3) == [4, 5, 6, 1, 2, 3]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=6) == [1, 2, 3, 4, 5, 6]
