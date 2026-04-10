import json

# Load JSON file
with open('hotel_data.json') as file:
    data = json.load(file)

print("Hotel Name:", data["hotel_name"])

print("\nGuest Details:")
for guest in data["guests"]:
    print(guest["name"], "staying in room", guest["room_number"])