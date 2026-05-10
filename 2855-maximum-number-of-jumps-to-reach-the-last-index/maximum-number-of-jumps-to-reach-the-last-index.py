class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i == n - 1:
                return 0

            best = -1

            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= target:
                    result = dfs(j)
                    if result != -1:
                        best = max(best, 1 + result)

            return best

        return dfs(0)
        