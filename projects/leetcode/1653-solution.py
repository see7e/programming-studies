class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        #n = len(s)
        # print('n:',n)
        #collection = {i:s.count(i) for i in s}
        # print('a:',collection['a'], 'b:',collection['b'])
        #return int((
        #    (n/collection['a'])+(n/collection['b'])
        #)/2)
        a_count = s.count('a')  # Total number of 'a's in the string
        min_deletions = a_count  # Initially, assume we delete all 'a's
        b_count = 0  # Counter for 'b's encountered

        for char in s:
            if char == 'a':
                a_count -= 1
            else:
                b_count += 1
            
            # Update minimum deletions required
            min_deletions = min(min_deletions, b_count + a_count)

        return min_deletions

        


sol = Solution()
print(sol.minimumDeletions("aababbab"))
print(sol.minimumDeletions("bbaaaaabb"))
