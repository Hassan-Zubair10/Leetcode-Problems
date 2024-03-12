class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum += i

        n = len(nums)
        total_sum = (n * (n+1)) // 2

        return total_sum - sum