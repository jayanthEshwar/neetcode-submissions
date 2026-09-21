class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
                continue
            return True
        return False
            