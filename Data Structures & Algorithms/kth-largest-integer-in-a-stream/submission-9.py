class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
