def rearrange(nums):
    if len(nums) <= 10:
        return nums
    genap = [num for num in nums if num % 2 == 0]
    ganjil = [num for num in nums if num % 2 != 0]

    return rearrange(genap) + rearrange(ganjil)

print (rearrange([3, 6, 8, 5, 4, 1, 4, 6]))