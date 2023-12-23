def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]

    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves


nums = [1,2,3]
result = min_moves(nums)
print(result)