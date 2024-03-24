def find_pair_indices(nums, target):
    """
    Finds a pair in the list that sums to the target number and returns their indices.

    Args:
        nums: A list of numbers.
        target: The target number.

    Returns:
        A list of two indices whose elements sum to the target number, or None if no such pair exists.
    """

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
