class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.lists = []  # Association with ToDoList objects
        
    def create_list(self, list_name):
        new_list = ToDoList(list_name, self)  # Pass self as the owner
        self.lists.append(new_list)
        return new_list
        
class ToDoList:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner  # Association with User object
        self.collaborators = []  # Association with multiple User objects
        self.items = []
        
    def add_collaborator(self, user):
        if user not in self.collaborators:
            self.collaborators.append(user)
            
class ToDoItem:
    def __init__(self, description, due_date, created_by):
        self.description = description
        self.due_date = due_date
        self.created_by = created_by  # Association with User object
        self.assigned_to = None  # Another association with User
        # Other attributes...
        
    def assign_to(self, user):
        self.assigned_to = user