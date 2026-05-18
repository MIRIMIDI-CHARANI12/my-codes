class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val=0
        c=0
        for num in nums:
            if c==0:
                val=num
            if num==val:
                c+=1
            else:
                c-=1
        return val
        