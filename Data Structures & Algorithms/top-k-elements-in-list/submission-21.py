class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map = {}
        # for n in nums:
        #     if n in map:
        #         map[n] += 1;
        #     else:
        #         map[n] = 1
        # result = sorted(map.items(),key=lambda item: item[1])
        # output = []
        # for i in range(len(result)-k, len(result)):
        #     output.append(result[i][0])
        # return output

        # Frequency array for numbers with frequency
        freq = [[] for i in range(len(nums)+1)]

        # Get frequency of each element
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        # initialize frequency array
        for n,c in count.items():
            freq[c].append(n)
        
        output = []
        for i in range (len(freq)-1,0,-1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output

        
        

