"""
Artefact Management System — Local Heritage Community (LHC)
ACCA5036 coursework. In-memory list of dictionaries (no database).
"""

# Allowed condition values for validation
ALLOWED_CONDITIONS = ("good", "damaged", "under repair")

# Master collection for this session
artefacts = []


def normalise_condition(text):
    """Return stripped lower-case condition text."""
    return text.strip().lower()


def find_artefact(name):
    """Return the first artefact dict matching name (case-insensitive), else None."""
    target = name.strip().lower()
    for item in artefacts:
        if item["name"].strip().lower() == target:
            return item
    return None


def add_artefact():
    """Add a new artefact after validating required fields and condition."""
    print("\n--- Add artefact ---")
    name = input("Artefact name: ").strip()
    category = input("Category: ").strip()
    location = input("Display location: ").strip()
    condition = normalise_condition(input("Condition (good / damaged / under repair): "))

    if not name or not category or not location:
        print("Error: name, category and location cannot be blank.")
        return
    if condition not in ALLOWED_CONDITIONS:
        print("Error: condition must be one of:", ", ".join(ALLOWED_CONDITIONS))
        return

    artefacts.append({
        "name": name,
        "category": category,
        "location": location,
        "condition": condition,
    })
    print("Artefact added successfully.")


def update_condition():
    """Update condition for an existing artefact found by name."""
    print("\n--- Update condition ---")
    name = input("Artefact name to update: ").strip()
    item = find_artefact(name)
    if item is None:
        print("Artefact not found.")
        return

    condition = normalise_condition(input("New condition (good / damaged / under repair): "))
    if condition not in ALLOWED_CONDITIONS:
        print("Error: condition must be one of:", ", ".join(ALLOWED_CONDITIONS))
        return

    item["condition"] = condition
    print("Condition updated for:", item["name"])


def view_artefacts():
    """Display all stored artefacts."""
    print("\n--- All artefacts ---")
    if not artefacts:
        print("No artefacts yet.")
        return
    for index, item in enumerate(artefacts, start=1):
        print(f"{index}. {item['name']} | {item['category']} | "
              f"{item['location']} | {item['condition']}")


def search_artefact():
    """Search by artefact name and show details if found."""
    print("\n--- Search artefact ---")
    name = input("Enter artefact name: ").strip()
    item = find_artefact(name)
    if item is None:
        print("Artefact not found.")
        return
    print("Name:", item["name"])
    print("Category:", item["category"])
    print("Location:", item["location"])
    print("Condition:", item["condition"])


def show_menu():
    """Print the main menu options."""
    print("\n===== LHC Artefact Management =====")
    print("1. Add artefact")
    print("2. Update condition")
    print("3. View all artefacts")
    print("4. Search artefact")
    print("5. Exit")


def main():
    """Menu loop until the user chooses exit."""
    running = True
    while running:
        show_menu()
        choice = input("Choose option (1-5): ").strip()
        if choice == "1":
            add_artefact()
        elif choice == "2":
            update_condition()
        elif choice == "3":
            view_artefacts()
        elif choice == "4":
            search_artefact()
        elif choice == "5":
            print("Goodbye.")
            running = False
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()
