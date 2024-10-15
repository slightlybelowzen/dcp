from bisect import bisect_left

def num_smaller_elements_to_right(nums: list[int]) -> list[int]:
  ans = []
  seen = []
  for i in range(len(nums) - 1, -1, -1):
    idx = bisect_left(seen, nums[i])
    seen.insert(idx, nums[i])
    ans.append(idx)
  ans.reverse()
  return ans


if __name__ == "__main__":
#   assert num_smaller_elements_to_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
  assert num_smaller_elements_to_right([5,2,6,1]) == [2,1,1,0]
