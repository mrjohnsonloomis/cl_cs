# Playlist Manager
# This program demonstrates four types of functions while managing a music playlist

# Type 1: Takes no arguments, returns nothing (void)
def display_menu():
    print("\n=== Playlist Manager ===")
    print("1. View all songs")
    print("2. View playlist duration")
    print("3. Find songs by artist")
    print("4. Get longest song")
    print("-" * 20)

# Type 2: Takes arguments, returns nothing (void)
def display_songs(song_list):
    print("\nYour Playlist:")
    song_number = 1
    for song in song_list:
        print(f"{song_number}. {song[0]} by {song[1]} - {song[2]} seconds")
        song_number = song_number + 1

# Type 3: Takes no arguments, returns value (fruitful)
def create_sample_playlist():
    # Returns a list of tuples: (song_name, artist, duration_in_seconds)
    return [
        ("Dreams", "The Cranberries", 281),
        ("Yellow", "Coldplay", 269),
        ("Africa", "Toto", 295),
        ("Take On Me", "a-ha", 225),
        ("Dreams", "Fleetwood Mac", 257)
    ]

# Type 4: Takes arguments, returns value (fruitful)
def find_songs_by_artist(playlist, artist):
    artist_songs = []
    for song in playlist:
        if artist.lower() in song[1].lower():
            artist_songs.append(song[0])
    return artist_songs

# Additional Type 4 example: Takes arguments, returns value (fruitful)
def get_longest_song(playlist):
    if not playlist:
        return None
    
    longest_duration = 0
    longest_song = ""
    
    for song in playlist:
        if song[2] > longest_duration:
            longest_duration = song[2]
            longest_song = song[0]
            
    return longest_song

# Program execution
def main():
    # Get our playlist using Type 3 function
    playlist = create_sample_playlist()
    
    while True:
        # Use Type 1 function to show menu
        display_menu()
        
        choice = input("Enter your choice (1-4, or 'q' to quit): ")
        
        if choice == 'q':
            break
            
        elif choice == '1':
            # Use Type 2 function to show all songs
            display_songs(playlist)
            
        elif choice == '2':
            # Calculate and display total duration
            total_seconds = sum(song[2] for song in playlist)
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            print(f"\nTotal playlist duration: {minutes} minutes, {seconds} seconds")
            
        elif choice == '3':
            # Use Type 4 function to find songs by artist
            artist = input("\nEnter artist name: ")
            found_songs = find_songs_by_artist(playlist, artist)
            if found_songs:
                print(f"\nSongs by {artist}:")
                for song in found_songs:
                    print(f"- {song}")
            else:
                print(f"\nNo songs found by {artist}")
                
        elif choice == '4':
            # Use another Type 4 function to find longest song
            longest = get_longest_song(playlist)
            print(f"\nLongest song in playlist: {longest}")
            
        else:
            print("\nInvalid choice. Please try again.")

# Start the program
main()

"""
Function Types Demonstrated:

Type 1 (No Arguments, No Return - Void):
- display_menu()
  Purpose: Shows available options
  Used when: You just need to display information

Type 2 (Takes Arguments, No Return - Void):
- display_songs(song_list)
  Purpose: Shows formatted list of songs
  Used when: You need to display data that's passed in

Type 3 (No Arguments, Returns Value - Fruitful):
- create_sample_playlist()
  Purpose: Creates and returns initial data
  Used when: You need to generate or get some data

Type 4 (Takes Arguments, Returns Value - Fruitful):
- find_songs_by_artist(playlist, artist)
- get_longest_song(playlist)
  Purpose: Processes data and returns results
  Used when: You need to compute something based on inputs

"""