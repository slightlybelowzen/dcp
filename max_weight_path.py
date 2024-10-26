def max_weight_path(wghts: list[list[int]]) -> int:
    ans = 0
    for row in wghts:
        ans += max(row)
    return ans

if __name__ == "__main__":
    assert max_weight_path([[1], [2, 3], [1, 5, 1]]) == 9
