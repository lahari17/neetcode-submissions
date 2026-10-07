class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1

        seen = dict(sorted(seen.items(), key = lambda x : x[1], reverse = True))

        lst=[]
        for i in range(k):
            lst.append(list(seen.keys())[i])
        return lst
            
