class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        lst_prefix = [0 for _ in range(len(cost))]
        lst_prefix[0], lst_prefix[1] = cost[0], cost[1]


        for i in range(2, len(cost)):
            lst_prefix[i] = min(lst_prefix[i-1], lst_prefix[i-2]) + cost[i]


        return (min(lst_prefix[-1], lst_prefix[-2]))