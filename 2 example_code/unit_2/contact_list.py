# Current contact management system
def display_contacts(dict):
    for item in dict.items():
        name, details = item
        print(f"Name: {name}")
        print(f"Role: {details['role']}")
        print(f"Email: {details['email']}")
        print("-" * 20)

def add_contact(dict, name, role, email):
    dict[name] = {"role": role, "email": email}
    print(f"Added {name} to contacts.")

def update_role(dict, name, new_role):
    dict[name]["role"] = new_role

def role_list(dict, target_role):
    role_list = []
    for name in dict:
        if dict[name]["role"] == target_role:
            role_list.append(name)
    return role_list


def main():
    contacts = {
        "Sarah Kim": {"role": "Sales Lead", "email": "sarah.k@company.com"},
        "Mike Chen": {"role": "Developer", "email": "mike.c@company.com"},
        "Lisa Wong": {"role": "Project Manager", "email": "lisa.w@company.com"}
    }
    # Test the functions
    display_contacts(contacts)
    add_contact(contacts,"Tom Lee", "Designer", "tom.l@company.com")
    print("\nAfter adding new contact:")
    display_contacts(contacts)

    desired_role = input('What role do you want contacts for?: ')
    print(role_list(contacts, desired_role))

main()