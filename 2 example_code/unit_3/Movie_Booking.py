class Movie_Booking:
    def __init__(self, movie_name, showtimes):
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
        # Check if showtime exists
        if showtime not in self.showtimes:
            print(f"Showtime {showtime} does not exist.")
            return False
        
        # Check if seat is available
        if seat_number not in self.seats_available[showtime]:
            print(f"Seat {seat_number} is not available for showtime {showtime}.")
            return False
        
        # Book the seat
        self.seats_available[showtime].remove(seat_number)
        self.booked_seats[showtime].append(seat_number)
        print(f"Seat {seat_number} booked for {self.movie_name} at {showtime}.")
        return True

    def cancel_booking(self, showtime, seat_number):
        # Check if showtime exists
        if showtime not in self.showtimes:
            print(f"Showtime {showtime} does not exist.")
            return False
        
        # Check if seat is booked
        if seat_number not in self.booked_seats[showtime]:
            print(f"Seat {seat_number} is not booked for showtime {showtime}.")
            return False
        
        # Cancel the booking
        self.booked_seats[showtime].remove(seat_number)
        self.seats_available[showtime].append(seat_number)
        # Sort seats to maintain order
        self.seats_available[showtime].sort()
        print(f"Booking for seat {seat_number} at {showtime} cancelled.")
        return True

    def display_available_seats(self, showtime):
        # Check if showtime exists
        if showtime not in self.showtimes:
            print(f"Showtime {showtime} does not exist.")
            return
        
        # Display available seats
        if len(self.seats_available[showtime]) == 0:
            print(f"No seats available for {self.movie_name} at {showtime}.")
        else:
            print(f"Available seats for {self.movie_name} at {showtime}: {self.seats_available[showtime]}")

    def update_showtimes(self, new_showtimes):
        # Initialize dictionaries for new showtimes
        new_seats_available = {}
        new_booked_seats = {}
        
        # Keep existing showtimes data
        for showtime in new_showtimes:
            if showtime in self.showtimes:
                # Keep existing data for this showtime
                new_seats_available[showtime] = self.seats_available[showtime]
                new_booked_seats[showtime] = self.booked_seats[showtime]
            else:
                # Initialize new data for this showtime
                new_seats_available[showtime] = list(range(1, self.total_seats + 1))
                new_booked_seats[showtime] = []
        
        # Update class attributes
        self.showtimes = new_showtimes
        self.seats_available = new_seats_available
        self.booked_seats = new_booked_seats
        print(f"Showtimes updated for {self.movie_name}.")

    def __str__(self):
        return self.movie_name

    def __len__(self):
        ''' Determines length based off of number of showtimes. '''
        return len(self.showtimes)


# Example usage
moana = Movie_Booking('Moana', ['2:30', '7:45'])
print(len(moana))