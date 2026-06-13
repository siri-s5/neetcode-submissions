class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set(nums)
        if len(nums)==len(list(seen)):
            return False
        return True