class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sub=""
        longest=0
        for i in s:
            if i not in sub:
                l=l+1
                sub=sub+i
                longest=max(longest,l)
            else:
                temp=sub.index(i)+1
                l=len(sub[temp:]+i)

                sub=sub[temp:]+i
        return longest