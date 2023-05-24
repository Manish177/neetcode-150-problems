class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        result=[]
        for i in nums:
            if i in dict1:
                dict1[i]=dict1[i]+1
            else:
                dict1[i]=1
        list1 = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
        j=0
        for i in list1:
            result.append(i[0])
            j=j+1
            if j==k:
                break
        return (result)


        