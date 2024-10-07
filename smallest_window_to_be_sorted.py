def window_unoptimised(array: list[int]) -> tuple[int, int]:
    s = sorted(array)
    left = right = None

    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i
    return left, right


def window(array: list[int]) -> tuple[int, int]:
    left = right = None
    curr_min = curr_max = array[0]
    for i, arr in enumerate(array):
        curr_max = max(curr_max, arr)
        if arr < curr_max:
            right = i
    for i in range(len(array) - 1, -1, -1):
        arr = array[i]
        curr_min = min(curr_min, arr)
        if arr > curr_min:
            left = i
    return left, right


if __name__ == "__main__":
    assert window_unoptimised([3, 7, 5, 6, 9]) == (1, 3)
    assert window([3, 7, 5, 6, 9]) == (1, 3)
