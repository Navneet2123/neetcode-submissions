class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Sum={}
        for i in range(len(nums)):
            number=target-nums[i]
            if number in Sum:
                return [Sum[number],i]
            Sum[nums[i]]=i
        return []
