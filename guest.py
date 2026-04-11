import json
import os

FILE_NAME = "guests.json"

# Load existing data
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add new guest
def add_guest():
    name = input("Enter guest name: ")
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")
    room = input("Enter room type: ")

    guest = {
        "name": name,
        "check_in": check_in,
        "check_out": check_out,
        "room": room
    }

    data = load_data()
    data.append(guest)
    save_data(data)

    print("✅ Guest added successfully!")

# View guests
def view_guests():
    data = load_data()
    if not data:
        print("No guest records found.")
        return

    print("\n📋 Guest List:")
    for i, guest in enumerate(data, start=1):
        print(f"\nGuest {i}")
        print("Name:", guest["name"])
        print("Check-in:", guest["check_in"])
        print("Check-out:", guest["check_out"])
        print("Room:", guest["room"])

# Main menu
while True:
    print("\n--- HOTEL MENU ---")
    print("1. Add Guest")
    print("2. View Guests")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_guest()
    elif choice == "2":
        view_guests()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
