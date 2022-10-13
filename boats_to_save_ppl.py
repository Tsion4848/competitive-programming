class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people) - 1
        res = 0
        
        people.sort()
        
        while i <= j:
            r = limit - people[j]
            j -= 1
            if people[i] <= r:
                i += 1
            res += 1
            
        return res
