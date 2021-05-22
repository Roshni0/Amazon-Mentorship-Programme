class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #inefficient sol
        for i in range(len(nums)): #loop through all elements in list
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: #check if matches target
                    return [i, j]
        #slightly more efficient
        for i in range(len(nums)): #loop through all elements in list
            if (target - nums[i]) in nums:
                j = nums.index(target - nums[i])
                return [i, j]
