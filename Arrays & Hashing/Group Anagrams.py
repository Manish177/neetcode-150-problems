class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for str in strs:
            count=[0]*26
            for i in str:
                count[ord(i)-ord('a')]=count[ord(i)-ord('a')]+1
        
            result[tuple(count)].append(str)
        return result.values()
                     
            