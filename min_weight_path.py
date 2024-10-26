def min_weight_path(wghts: list[list[int]]) -> int:
    ans = 0
    for row_idx, row in enumerate(wghts):
        for col_idx, col in enumerate(row):
            ...
    return ans

if __name__ == "__main__":
    assert min_weight_path([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11
    assert min_weight_path([[-10]]) == -10

