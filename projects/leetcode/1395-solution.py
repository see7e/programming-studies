class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        if n < 3:
            return 0

        count = 0
        
        for j in range(1, n - 1):
            left_smaller = left_greater = 0
            right_smaller = right_greater = 0
            
            # Count elements before j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            # Count elements after j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_greater += 1
            
            # Calculate valid teams
            count += left_smaller * right_greater + left_greater * right_smaller
        
        return count

sol = Solution()
print(sol.numTeams([2,5,3,4,1]))
print(sol.numTeams([2,1,3]))
print(sol.numTeams([1,2,3,4]))
