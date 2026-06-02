class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1;
            else:
                map[n] = 1
        result = sorted(map.items(),key=lambda item: item[1])
        output = []
        for i in range(len(result)-k, len(result)):
            output.append(result[i][0])
        return output
