import json

# Load JSON data
with open('hotel_data.json') as file:
    data = json.load(file)

print("===== HOTEL DETAILS =====")
print("Hotel Name:", data["hotel_name"])
print("Location:", data["location"])

print("\n===== GUEST DETAILS =====")
for guest in data["guests"]:
    print("Name:", guest["name"])
    print("Room:", guest["room_number"])
    print("Check-in:", guest["check_in"])
    print("Check-out:", guest["check_out"])
    print("----------------------")

# Example: Change a guest name
data["guests"][0]["name"] = "Updated Name"

print("\nAfter Updating Name:")
print(data["guests"][0]["name"])