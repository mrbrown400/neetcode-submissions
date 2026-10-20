class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in res:
                return [res[diff], idx]
            else:
                res[num] = idx
        