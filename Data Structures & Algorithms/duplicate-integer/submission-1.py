class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp={}
        for i in nums:
            if i in mpp.keys():
                return True
            mpp[i]=1+mpp.get(i,0)
        return False
