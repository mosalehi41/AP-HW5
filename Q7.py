nums = [1, 2, 3, 4, 5, 12, 7, 8, 9, 10, 11, 18, 13, 14, 15, 16, 17, 6]


print(sorted(set([nums[i] for i in range(len(nums)) if (i + 1) % 6 == 0 and nums[i] % 6 == 0 ])))


