class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # else:
            #     for j in range(i+1,len(nums)):
            #         if j > i+1 and nums[j] == nums[j-1]:
            #             continue
            #         for k in range(j+1, len(nums)):
            #             if k > j+1 and nums[k] == nums[k-1]:
            #                 continue
            #             if nums[i] + nums [j] + nums [k] == 0:
            #                 result.append([nums[i], nums [j], nums [k]])
            #             else:
            #                 continue
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l = l+1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[i]+nums[l]+nums[r] == 0:
                    result.append([nums[i], nums [l], nums [r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result                        

        
        