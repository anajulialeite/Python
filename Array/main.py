def maxSubArray(self, nums: list[int]) -> int:
    glob = -126335183676512786
    loc = 0

    for value in nums:
        loc = max(value, value+loc)
        glob = max(glob, loc)

    return glob