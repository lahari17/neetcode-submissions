class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countf = {}
        for num in nums:
            countf[num] = countf.get(num,0)+1

        result = dict(sorted(countf.items(), key = lambda x : x[1], reverse = True))
        return list(result.keys())[:k]
        


            


        