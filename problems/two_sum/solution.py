# ============================================================
# Problem: Two Sum
# ============================================================
# Given a list of integers `nums` and a target integer,
# return the indices of the two numbers that add up to target.
#
# You may assume exactly one solution exists, and you may not
# use the same element twice.
#
# Example:
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]   (because nums[0] + nums[1] == 9)
# ============================================================


def solve(nums: list[int], target: int) -> list[int]:
    # Your solution here
    target_indice_dict = {}
    for i, num in enumerate(nums):
        if target - num in target_indice_dict:
            return [target_indice_dict[target - num], i]
        target_indice_dict[num] = i

    raise NotImplementedError
