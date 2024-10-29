def min_time_diff(times: list[str]) -> int:
    ...

if __name__ == "__main__":
    assert min_time_diff(["23:59","00:00"]) == 1
    assert min_time_diff(["23:59","00:00", "00:00"]) == 0
