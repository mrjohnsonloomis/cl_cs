# Text Message Analyzer
# This program analyzes text messages for length, word count, and hashtag usage
# First we'll show how to do it without functions (linear approach)
# Then we'll improve it using functions (modular approach)

print("APPROACH 1: Linear Programming (Without Functions)")
print("-" * 50)

# Sample messages to analyze
messages = [
    "Having a great time at the beach! #sunshine #vacation",
    "Just finished my homework",
    "Movie night with friends #fun #weekend #movies"
]

# Linear approach - analyzing messages without functions
print("Analyzing messages...")
for message in messages:
    # Count characters
    char_count = len(message)
    print(f"\nMessage: {message}")
    print(f"Character count: {char_count}")
    
    # Count words
    words = message.split()
    word_count = len(words)
    print(f"Word count: {word_count}")
    
    # Find hashtags
    hashtags = []
    for word in words:
        if word.startswith('#'):
            hashtags.append(word)
    if hashtags:
        print(f"Hashtags found: {hashtags}")
    else:
        print("No hashtags found")

print("\n\nAPPROACH 2: Modular Programming (With Functions)")
print("-" * 50)

# Function Type 1: Takes no arguments, returns nothing (void)
def print_separator():
    print("\n" + "-" * 50 + "\n")

# Function Type 2: Takes arguments, returns nothing (void)
def display_message_info(msg):
    print(f"Message: {msg}")

# Function Type 3: Takes no arguments, returns value (fruitful)
def get_sample_messages():
    return [
        "Having a great time at the beach! #sunshine #vacation",
        "Just finished my homework",
        "Movie night with friends #fun #weekend #movies"
    ]

# Function Type 4: Takes arguments, returns value (fruitful)
def count_hashtags(message):
    words = message.split()
    hashtag_list = []
    for word in words:
        if word.startswith('#'):
            hashtag_list.append(word)
    return hashtag_list

# Main analysis using functions
messages = get_sample_messages()

for message in messages:
    print_separator()
    display_message_info(message)
    
    # Using built-in functions and string methods we already know
    print(f"Character count: {len(message)}")
    print(f"Word count: {len(message.split())}")
    
    # Using our custom hashtag counter function
    hashtags = count_hashtags(message)
    if hashtags:
        print(f"Hashtags found: {hashtags}")
    else:
        print("No hashtags found")

# Benefits of the functional approach:
# 1. Code is more organized and easier to read
# 2. Functions can be reused
# 3. Easier to test and debug
# 4. Easier to modify or extend functionality