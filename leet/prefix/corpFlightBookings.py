class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        rtn = [0] * n
        for s, e, b in bookings:
            rtn[s-1] += b
            if e < n:
                rtn[e] -= b
            
        return itertools.accumulate(rtn)