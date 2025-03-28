class ToDoItem:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.priority = "Medium"
        self.completed = False
        self.estimated_minutes = 30
        self.snoozed_until = None
    
    def __str__(self):
        status = "COMPLETED" if self.completed else "PENDING"
        snoozed = f" (Snoozed until: {self.snoozed_until})" if self.snoozed_until else ""
        return f"{status}: {self.description} - Due: {self.due_date} - Priority: {self.priority}{snoozed}"
    
    def __len__(self):
        return self.estimated_minutes
    
    def mark_complete(self):
        self.completed = True
        return "Task marked as complete!"
    
    def edit_description(self, new_description):
        self.description = new_description
        return "Description updated successfully!"
    
    def change_priority(self, new_priority):
        self.priority = new_priority
        return "Priority updated successfully!"
    
    def set_time_estimate(self, minutes):
        self.estimated_minutes = minutes
        return f"Time estimate set to {minutes} minutes!"
    
    def snooze(self, until_date):
        self.snoozed_until = until_date
        return f"Task snoozed until {until_date}!"

class ToDoList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_item(self):
        task = input('What do you need to do?: ')
        date = input('By when?: ')
        to_add = ToDoItem(task, date)
        self.add_item(to_add)

    def __str__(self):
        ret = ''
        for item in self.items:
            ret += f'{item.description} '
        return ret
    


# Client code
def main():
    # Create two tasks
    homework = ToDoItem("Complete Python assignment", "2025-03-30")
    shopping = ToDoItem("Go grocery shopping", "2025-03-28")
    
    # Test methods
    print(homework)
    print(f"Estimated time: {len(homework)} minutes")
    
    homework.set_time_estimate(45)
    homework.edit_description("Finish Python class project")
    homework.mark_complete()
    print(homework)
    
    print(shopping)
    shopping.change_priority("Low")
    shopping.snooze("2025-04-01")
    print(shopping)

    today = ToDoList('Todays tasks')
    today.add_item(homework)
    today.add_item(shopping)
    today.create_item()

    print(today)

main()