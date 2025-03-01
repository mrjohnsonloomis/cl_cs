class Movie_Booking:
    """
    A class that simulates a movie ticket booking system.
    """
    
    def __init__(self, movie_name, showtimes):
        """
        Initialize a new MovieTicketSystem object.
        Args:
            movie_name (str): The name of the movie.
            showtimes (list): A list of showtimes for the movie.
        """
        self.movie_name = movie_name
        self.showtimes = showtimes
        self.total_seats = 5
        self.seats_available = self._initialize_seats_available(self.total_seats)
        self.booked_seats = self._initialize_booked_seats()
        
    def _initialize_seats_available(self, total_seats):
        seats_available = {}
        for showtime in self.showtimes:
            # Create a list of seat numbers from 1 to total_seats
            seats_available[showtime] = list(range(1, total_seats + 1))
        return seats_available
    
    def _initialize_booked_seats(self):
        booked_seats = {}
        for showtime in self.showtimes:
            booked_seats[showtime] = []
        return booked_seats
    
    def book_seat(self, showtime, seat_number):
        pass
    
    def cancel_booking(self, showtime, seat_number):
    
        pass
    
    def display_available_seats(self, showtime):
        pass
    
    def update_showtimes(self, new_showtimes):
        pass
    
    def __str__(self):
        pass
    
    def __len__(self):
        pass
    