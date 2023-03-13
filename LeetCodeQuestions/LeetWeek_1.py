def runningSum(self, nums: List[int]) -> List[int]:
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    :rtype: list with sums
    """
    # My solution: # beats 45% of other solutions
    nums_sums = []

    for i, number in enumerate(nums):
        if i == 0:
            nums_sums.append(number)
        else:
            sum = number + nums_sums[i - 1]
            nums_sums.append(sum)
    return nums_sums

    # Suggested solution for better performance:

    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums