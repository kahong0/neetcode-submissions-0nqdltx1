class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashset
        hashset = set()

        # go through every value in nums
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False