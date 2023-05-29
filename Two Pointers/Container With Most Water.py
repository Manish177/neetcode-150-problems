class Solution:
    def maxArea(self, height: List[int]) -> int:
        w=(len(height)-1)
        L1=0
        L2=len(height)-1
        max_area=min(height[0],height[-1])*w
        while L1<L2:
            if height[L1]<height[L2]:
                L1=L1+1
            else:
                L2=L2-1   
            w=w-1
            if min(height[L1],height[L2])*w>max_area:
                max_area=min(height[L1],height[L2])*w
        return max_area