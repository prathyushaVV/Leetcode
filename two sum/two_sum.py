class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        output = 0
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in store:
                return [store[diff], i]
            else:
                store[nums[i]] = i
