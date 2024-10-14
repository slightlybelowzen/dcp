def min_num_boats(wghts: list[int], k: int):
  wghts.sort(reverse=True)
  ans = 0
  i, j = 0, len(wghts) - 1
  while i <= j:
    if wghts[i] + wghts[j] <= k:
      j -= 1
    ans += 1
    i += 1
  return ans


if __name__ == "__main__":
  assert min_num_boats([100, 200, 150, 80], 200) == 3
  assert min_num_boats([1, 2], 3) == 1
  assert min_num_boats([3,5,3,4], 5) == 4
