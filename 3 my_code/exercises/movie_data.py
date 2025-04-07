'''
YOUR TASK:

(OPTIONAL) Data Loading and Processing:

1) Read the movie theater data from the generated file
2) Organize the data by theater, movie, and showtime
3) Calculate total tickets sold and revenue for each theater and movie


Basic Visualization Steps (Part 1 concepts):

1) Create a line plot showing daily ticket sales over time for each theater
2) Create a bar chart comparing total revenue for each movie
3) Create a scatter plot of ticket prices vs. concession sales

'''
# Read the data from the file
with open('movie_theater_data.txt', 'r') as file:
    next(file)  # Skip header
    for line in file:
        # TODO: Parse each line and organize data by theater, movie, and showtime
        pass

    
# Task 1: Read and process the data
dates = []
theaters = []
movies = []
tickets_by_theater = {}  # Dictionary to store ticket data by theater
revenue_by_movie = {}    # Dictionary to store revenue data by movie
concessions = {}         # Dictionary to store concession data
showtime_data = {}       # Dictionary to store showtime data



# Calculate totals and averages
total_tickets_by_theater = {}
total_revenue_by_movie = {}
avg_concession_by_theater = {}
