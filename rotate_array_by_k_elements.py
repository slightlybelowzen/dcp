def solve(nums: list[int], k: int) -> list[int]:
    i, j = 0, len(nums) - 1
    return nums


if __name__ == "__main__":
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=2) == [3, 4, 5, 6, 1, 2]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=3) == [4, 5, 6, 1, 2, 3]
    assert solve(nums=[1, 2, 3, 4, 5, 6], k=6) == [1, 2, 3, 4, 5, 6]
