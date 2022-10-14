class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n

        for b in bookings:
            res[b[0] - 1] += b[2]
            if b[1] < n:
                res[b[1]] -= b[2]

        for i in range(1, n):
            res[i] += res[i - 1]

        return res
