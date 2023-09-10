def rearrange(nums):
    if len(nums) <= 5:
        return nums
    genap = [num for num in nums if num % 2 == 0]
    ganjil = [num for num in nums if num % 2 != 0]

    return rearrange(genap) + rearrange(ganjil)

print (rearrange([13, 17, 18, 15, 4, 22,35]))