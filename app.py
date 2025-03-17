import streamlit as st
import requests

# Base URL of your FastAPI backend
API_URL = "http://127.0.0.1:8000"

# Functions to interact with the FastAPI endpoints

def get_coaches(skip=0, limit=100):
    response = requests.get(f"{API_URL}/coaches", params={"skip": skip, "limit": limit})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching coaches")
        return []

def create_coach(nom, prenom, email):
    payload = {"nom": nom, "prenom": prenom, "email": email}
    response = requests.post(f"{API_URL}/coaches", json=payload)
    if response.status_code == 200:
        st.success("Coach created successfully!")
        return response.json()
    else:
        st.error("Error creating coach")
        return None

def update_coach(coach_id, nom, prenom, email):
    payload = {"nom": nom, "prenom": prenom, "email": email}
    response = requests.put(f"{API_URL}/coaches/{coach_id}", json=payload)
    if response.status_code == 200:
        st.success("Coach updated successfully!")
        return response.json()
    else:
        st.error("Error updating coach")
        return None

def delete_coach(coach_id):
    response = requests.delete(f"{API_URL}/coaches/{coach_id}")
    if response.status_code == 200:
        st.success("Coach deleted successfully!")
        return response.json()
    else:
        st.error("Error deleting coach")
        return None

# ------------------------------
# Streamlit UI
# ------------------------------

st.title("Coach Management")

# Sidebar menu for navigation
menu = st.sidebar.selectbox("Menu", ["View Coaches", "Add Coach", "Update Coach", "Delete Coach"])

if menu == "View Coaches":
    st.header("List of Coaches")
    coaches = get_coaches()
    if coaches:
        for coach in coaches:
            st.write(f"ID: {coach['id_coach']} - {coach['nom']} {coach['prenom']} - {coach['email']}")
    else:
        st.write("No coaches found.")

elif menu == "Add Coach":
    st.header("Add a New Coach")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prenom")
    email = st.text_input("Email")
    if st.button("Create Coach"):
        result = create_coach(nom, prenom, email)
        if result:
            st.write("Created Coach:", result)

elif menu == "Update Coach":
    st.header("Update a Coach")
    coach_id = st.number_input("Coach ID", min_value=1, step=1)
    nom = st.text_input("New Nom")
    prenom = st.text_input("New Prenom")
    email = st.text_input("New Email")
    if st.button("Update Coach"):
        result = update_coach(coach_id, nom, prenom, email)
        if result:
            st.write("Updated Coach:", result)

elif menu == "Delete Coach":
    st.header("Delete a Coach")
    coach_id = st.number_input("Coach ID to Delete", min_value=1, step=1)
    if st.button("Delete Coach"):
        result = delete_coach(coach_id)
        if result:
            st.write(result)
