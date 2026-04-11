import streamlit as st
import json
import os

FILE_NAME = "guests.json"

# Load data
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

st.title("🏨 Hotel Guest Management System")

menu = st.sidebar.selectbox("Menu", ["Add Guest", "View Guests", "Search Guest", "Delete Guest"])

# ADD GUEST
if menu == "Add Guest":
    st.subheader("Add Guest Details")

    name = st.text_input("Guest Name")
    check_in = st.date_input("Check-in Date")
    check_out = st.date_input("Check-out Date")
    room = st.text_input("Room Type")

    if st.button("Add Guest"):
        guest = {
            "name": name,
            "check_in": str(check_in),
            "check_out": str(check_out),
            "room": room
        }

        data = load_data()
        data.append(guest)
        save_data(data)

        st.success("✅ Guest added successfully!")

# VIEW GUESTS
elif menu == "View Guests":
    st.subheader("Guest List")

    data = load_data()
    if data:
        for i, guest in enumerate(data, start=1):
            st.write(f"### Guest {i}")
            st.write(guest)
    else:
        st.warning("No guests found")

# SEARCH GUEST
elif menu == "Search Guest":
    st.subheader("Search Guest")

    name = st.text_input("Enter name to search")

    if st.button("Search"):
        data = load_data()
        found = False

        for guest in data:
            if guest["name"].lower() == name.lower():
                st.success("Guest Found")
                st.write(guest)
                found = True

        if not found:
            st.error("Guest not found")

# DELETE GUEST
elif menu == "Delete Guest":
    st.subheader("Delete Guest")

    name = st.text_input("Enter name to delete")

    if st.button("Delete"):
        data = load_data()
        new_data = [g for g in data if g["name"].lower() != name.lower()]

        if len(data) == len(new_data):
            st.error("Guest not found")
        else:
            save_data(new_data)
            st.success("Guest deleted successfully")
