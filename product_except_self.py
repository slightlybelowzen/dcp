def main():
    nums = [1, 2, 3, 4, 5]
    expected = [120, 60, 40, 30, 24]
    prefix_products = []
    suffix_products = []
    ans = []
    for num in nums:
        prefix_products.append(
            num * prefix_products[-1]
        ) if prefix_products else prefix_products.append(num)
    for num in reversed(nums):
        suffix_products.append(
            num * suffix_products[-1]
        ) if suffix_products else suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))
    for i in range(len(nums)):
        if i == 0:
            ans.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            ans.append(prefix_products[i - 1])
        else:
            ans.append(prefix_products[i - 1] * suffix_products[i + 1])
    assert expected == ans


if __name__ == "__main__":
    main()
