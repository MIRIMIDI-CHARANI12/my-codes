class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        r = n - 1
        l = w = leftmax = rightmax = 0

        while l < r:
            if height[l] < height[r]:
                w += max(0, leftmax - height[l])
                leftmax = max(leftmax, height[l])
                l += 1
            else:
                w += max(0, rightmax - height[r])
                rightmax = max(rightmax, height[r])
                r -= 1

        return w
        