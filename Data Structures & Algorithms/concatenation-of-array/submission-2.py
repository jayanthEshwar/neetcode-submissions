class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r=len(nums)
        ans=nums
        for i in range(0,r):
            ans.append(nums[i])
        return ans