class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prefix_lst = [0 for _ in range(len(nums))]
        if len(prefix_lst) == 1:
            return nums[0]

        elif len(prefix_lst) == 2:
            return max(nums[1], nums[0])
        prefix_lst[0], prefix_lst[1], prefix_lst[2] = nums[0], nums[1], nums[2]+nums[0]

        for i in range(3, len(nums)):
            prefix_lst[i] = max(prefix_lst[i-2], prefix_lst[i-3]) + nums[i]

        return max(prefix_lst[-1], prefix_lst[-2])