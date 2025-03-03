class EventPlanner:
    # Class to manage events including guest lists, RSVPs, and budget
    
    def __init__(self, event_name, event_date, event_location):
        # Initialize a new event with basic info
        self.event_name = event_name
        self.event_date = event_date
        self.event_location = event_location
        self.max_capacity = 50     # Default value
        self.budget = 1000.00      # Default value
        self.guest_list = []
        self.rsvp_yes = []
        self.rsvp_no = []
        self.expenses = {}
    
    def add_guest(self, guest_name):
        # Add a guest to the guest list
        self.guest_list.append(guest_name)
    
    def remove_guest(self, guest_name):
        # Remove a guest from the guest list and any RSVP lists
        if guest_name in self.guest_list:
            self.guest_list.remove(guest_name)
        
        if guest_name in self.rsvp_yes:
            self.rsvp_yes.remove(guest_name)
        
        if guest_name in self.rsvp_no:
            self.rsvp_no.remove(guest_name)
    
    def rsvp(self, guest_name, attending):
        # Record a guest's RSVP (attending is boolean)
        if guest_name in self.guest_list:
            # Remove from both RSVP lists first to handle changes
            if guest_name in self.rsvp_yes:
                self.rsvp_yes.remove(guest_name)
            if guest_name in self.rsvp_no:
                self.rsvp_no.remove(guest_name)
            
            # Add to appropriate RSVP list
            if attending:
                self.rsvp_yes.append(guest_name)
            else:
                self.rsvp_no.append(guest_name)
            return True
        return False
    
    def add_expense(self, category, amount):
        # Add an expense to a category
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
    
    def set_max_capacity(self, max_capacity):
        # Update the maximum capacity
        self.max_capacity = max_capacity
    
    def set_budget(self, budget):
        # Update the budget
        self.budget = budget
    
    def get_available_capacity(self):
        # Calculate and return remaining capacity
        return self.max_capacity - len(self.rsvp_yes)
    
    def get_budget_remaining(self):
        # Calculate and return remaining budget
        total_expenses = 0
        for amount in self.expenses.values():
            total_expenses += amount
        return self.budget - total_expenses
    
    def get_attending_count(self):
        # Return the number of confirmed attendees
        return len(self.rsvp_yes)
    
    def get_rsvp_status(self, guest_name):
        # Return whether a guest has RSVP'd and their response
        if guest_name in self.rsvp_yes:
            return "Attending"
        elif guest_name in self.rsvp_no:
            return "Not attending"
        elif guest_name in self.guest_list:
            return "No response yet"
        else:
            return "Not invited"
    
    def display_guest_list(self):
        # Return a formatted string of all guests and their RSVP status
        result = ""
        for guest in self.guest_list:
            result += f"{guest}: {self.get_rsvp_status(guest)}\n"
        return result
    
    def display_budget_summary(self):
        # Return a formatted summary of budget and expenses
        result = f"Budget: ${self.budget:.2f}\n"
        result += "Expenses:\n"
        
        for category, amount in self.expenses.items():
            result += f"  {category}: ${amount:.2f}\n"
        
        result += f"Remaining: ${self.get_budget_remaining():.2f}"
        return result


def popular_events(event_list):
    # Takes in a list of EventPlanner objects and returns a list of strings
    # representing only those events that have 80% or more of their capacity filled
    popular_event_names = []
    
    for event in event_list:
        # Calculate percentage of capacity filled
        capacity_filled = len(event.rsvp_yes) / event.max_capacity
        
        # Check if 80% or more of capacity is filled
        if capacity_filled >= 0.8:
            popular_event_names.append(event.event_name)
    
    return popular_event_names


def main():
    # Create several event planner objects
    wedding = EventPlanner("Smith-Johnson Wedding", "2023-06-15", "Grand Ballroom")
    conference = EventPlanner("Tech Conference", "2023-07-22", "Convention Center")
    birthday = EventPlanner("Jake's 30th Birthday", "2023-08-05", "Backyard")
    reunion = EventPlanner("Class Reunion", "2023-09-10", "High School Gym")
    
    # Update capacity and budget for each event
    wedding.set_max_capacity(100)
    wedding.set_budget(5000.00)
    
    conference.set_max_capacity(200)
    conference.set_budget(10000.00)
    
    birthday.set_max_capacity(30)
    birthday.set_budget(500.00)
    
    reunion.set_max_capacity(150)
    reunion.set_budget(3000.00)
    
    # Add guests and RSVPs to wedding (90% capacity)
    for i in range(1, 101):
        guest_name = f"Wedding Guest {i}"
        wedding.add_guest(guest_name)
        # Make 90 guests RSVP yes
        if i <= 90:
            wedding.rsvp(guest_name, True)
        else:
            wedding.rsvp(guest_name, False)
    
    # Add guests and RSVPs to conference (50% capacity)
    for i in range(1, 201):
        guest_name = f"Conference Attendee {i}"
        conference.add_guest(guest_name)
        # Make 100 attendees RSVP yes
        if i <= 100:
            conference.rsvp(guest_name, True)
        else:
            conference.rsvp(guest_name, False)
    
    # Add guests and RSVPs to birthday (90% capacity)
    for i in range(1, 31):
        guest_name = f"Birthday Guest {i}"
        birthday.add_guest(guest_name)
        # Make 27 guests RSVP yes
        if i <= 27:
            birthday.rsvp(guest_name, True)
        else:
            birthday.rsvp(guest_name, False)
    
    # Add guests and RSVPs to reunion (70% capacity)
    for i in range(1, 151):
        guest_name = f"Reunion Attendee {i}"
        reunion.add_guest(guest_name)
        # Make 105 attendees RSVP yes
        if i <= 105:
            reunion.rsvp(guest_name, True)
        else:
            reunion.rsvp(guest_name, False)
    
    # Create a list of event planner objects
    events = [wedding, conference, birthday, reunion]
    
    # Call popular_events function
    popular = popular_events(events)
    
    # Print the result
    print("Popular events (80% or more capacity filled):")
    for event in popular:
        print(f"- {event}")



main()