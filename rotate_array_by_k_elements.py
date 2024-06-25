def solve(nums: list[int], k: int) -> list[int]:
    # this is the less memory efficient way
    return nums[k:] + nums[0:k]
    # i, j = 0, len(nums) - 1


if __name__ == "__main__":
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=2) == [3, 4, 5, 6, 1, 2]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=3) == [4, 5, 6, 1, 2, 3]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=6) == [1, 2, 3, 4, 5, 6]
