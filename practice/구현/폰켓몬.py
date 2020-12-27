def solution(nums):
    pickNum = len(nums)//2
    nums = list(set(nums))
    return min(pickNum, len(nums))
