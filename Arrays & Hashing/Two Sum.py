class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index,i in enumerate(nums):
            if i in dict:
                return [dict[i],index]
            else:
                dict[target-i]=index