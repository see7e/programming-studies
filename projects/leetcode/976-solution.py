class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if not 3 <= len(nums) and len(nums) <= 10000:
            return 0 # Breaks problem constraints

        # iterate over the possibilities
        nums.sort()
        for idx in range(len(nums) -3, -1, -1):
            if not nums[idx] >= 1 and nums[idx] <= 1000000:
                return 0 # Breaks problem constraints
            if nums[idx] + nums[idx + 1] > nums[idx + 2]:
                sum = nums[idx] + nums[idx + 1] + nums[idx + 2]
                result = sum if sum >= result else result
        return result

nums1 = [2,1,2]
nums2 = [1,2,1,10]
sol = Solution()
print(sol.largestPerimeter(nums1))
print(sol.largestPerimeter(nums2))
