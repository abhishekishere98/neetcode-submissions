class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for i in range (len(numbers)-1):
        #     for j in range (len(numbers)-1, -1, -1):
        #         if numbers[i] + numbers[j] == target and i<j :
        #             return [i+1,j+1]

        l,r = 0,len(numbers)-1

        while l < r :
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] == target:
                return [l+1,r+1]


        