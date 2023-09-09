def rearrange(nums):
    # base case
    if len(nums) <= 10:
        return nums
    # recursive case
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 != 0]

    return rearrange(even_nums) + rearrange(odd_nums)

print (rearrange([3, 6, 8, 5, 4, 1, 4, 6]))