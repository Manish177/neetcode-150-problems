class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1={}

        for i in s1:
            if i in dict1:
                dict1[i]=dict1[i]+1
            else:
                dict1[i]=1
        for i in range(len(s2)-len(s1)+1): 
            dict2={}
            for j in s2[i:i+len(s1)]:
                if j in dict2:
                    dict2[j]=dict2[j]+1
                else:
                    dict2[j]=1
            if dict1==dict2:
                return True
        return False