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


def pivotIndex(self, nums: List[int]) -> int:
    """
    Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
    created after: https://www.youtube.com/watch?v=u89i60lYx8U
    structure: build up sum each from left and right 'side' of the list. if they are equal, there is a pivot ('middle'), return the pivot's position
    if not, return -1, there is no pivot
    :rtype: object
    """
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum
        if left_sum == right_sum: # check if the current position is th pivot index
            return i # return the index not the actual value
        left_sum += nums[i]
    return -1