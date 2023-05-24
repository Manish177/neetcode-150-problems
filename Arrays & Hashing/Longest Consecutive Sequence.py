class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        longest=1
        temp=1
        nums=sorted(nums)
        prev=nums[0]
        for i in nums[1:]:
            if i==prev+1:
                prev=i
                temp=temp+1
                if longest<temp:
                    longest=temp
            elif i==prev:
                prev=i
            else:
                prev=i
                temp=1
        return longest