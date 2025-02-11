# Current contact management system
contacts = {
    "Sarah Kim": {"role": "Sales Lead", "email": "sarah.k@company.com"},
    "Mike Chen": {"role": "Developer", "email": "mike.c@company.com"},
    "Lisa Wong": {"role": "Project Manager", "email": "lisa.w@company.com"}
}

def display_contacts():
    for item in contacts.items():
        name, details = item
        print(f"Name: {name}")
        print(f"Role: {details['role']}")
        print(f"Email: {details['email']}")
        print("-" * 20)

def add_contact(name, role, email):
    contacts[name] = {"role": role, "email": email}
    print(f"Added {name} to contacts.")

# Test the functions
display_contacts()
add_contact("Tom Lee", "Designer", "tom.l@company.com")
print("\nAfter adding new contact:")
display_contacts()