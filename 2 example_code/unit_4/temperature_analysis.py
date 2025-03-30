# Temperature Data Analysis Program

def read_temperature_data(filename):
    """
    Read temperature data from a CSV file and return it as a 2D list.
    The first row should be the header with city names.
    """
    data = []
    with open('temperature_data.csv') as file:
        header = file.readline() # this gets rid of the header, proceed as normal after this
        
    # TODO: Open the file and read its contents
    # TODO: Convert each line to a list of values
    # TODO: Return the 2D list of data
    
    return data

def calculate_city_statistics(data):
    """
    Calculate statistics for each city:
    - Average temperature
    - Highest temperature (and which day)
    - Lowest temperature (and which day)
    Returns a dictionary with city names as keys and statistics as values
    """
    city_stats = {}
    # TODO: Get the city names from the header row
    # TODO: For each city, calculate average, min, and max temperatures
    # TODO: Store the results in the city_stats dictionary
    
    return city_stats

def find_temperature_trends(data):
    """
    Find interesting temperature trends:
    - Which city had the most consistent temperatures (lowest range)
    - Which city had the most variable temperatures (highest range)
    - Which day was the hottest across all cities (highest average)
    - Which day was the coldest across all cities (lowest average)
    """
    trends = {}
    # TODO: Calculate the temperature range for each city
    # TODO: Calculate the average temperature for each day
    # TODO: Determine which city had the smallest and largest temperature range
    # TODO: Determine which day had the highest and lowest average temperature
    
    return trends

def print_report(city_stats, trends):
    """
    Print a formatted report of the temperature analysis.
    """
    print("\n===== TEMPERATURE ANALYSIS REPORT =====\n")
    
    # TODO: Print city statistics (average, min, max)
    # TODO: Print interesting trends
    
    print("\n======================================")

def main():
    # File path
    filename = "temperature_data.csv"
    
    # Step 1: Read the data
    print("Reading temperature data...")
    temperature_data = read_temperature_data(filename)
    
    if temperature_data:
        # Print the first few lines of data to verify
        print(f"Successfully read data for {len(temperature_data[0]) - 1} cities over {len(temperature_data) - 1} days.")
        print("First few readings:")
        for i in range(min(4, len(temperature_data))):
            print(temperature_data[i])
        
        # Step 2: Calculate statistics for each city
        print("\nCalculating city statistics...")
        city_stats = calculate_city_statistics(temperature_data)
        
        # Step 3: Find temperature trends
        print("Analyzing temperature trends...")
        trends = find_temperature_trends(temperature_data)
        
        # Step 4: Print the report
        print_report(city_stats, trends)
    else:
        print("Error: Could not read temperature data.")

# Run the program
main()