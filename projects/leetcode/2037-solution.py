from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        # Sort the array to see the best disposition of students and seats 
        seats.sort()
        students.sort()

        # 1 <= n <= 100
        for n in range(0, len(seats)):
            # Check the surrowndings of the available seats if theres a student nearby
            if not students[n] == seats[n]:
                seats_to_move = abs(students[n] - seats[n])
            else:
                # Dont need to move anyone
                continue
            result += seats_to_move
        return result

sol = Solution()
# CASE 1
print(sol.minMovesToSeat([3,1,5],[2,7,4]))
    
# CASE 2
print(sol.minMovesToSeat([4,1,5,9], [1,3,2,6]))
    
# CASE 3
print(sol.minMovesToSeat([3,1,5],[1,3,2,6]))
