class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        if n <= 0:
            raise ValueError("Invalid value of n.")
        
        self.seats = list(range(1, n + 1)) # Initialize available seats from 1 to n.

    def reserve(self):
        """
        :rtype: int
        """
        if not self.seats:
            return -1  # No available seats.
        
        reserved_seat = heapq.heappop(self.seats) # Get the smallest available seat.
        return reserved_seat

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        if seatNumber > 0:
            heapq.heappush(self.seats, seatNumber) # Add the seat back to available seats.


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)