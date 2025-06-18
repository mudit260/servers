import streamlit as st

# === Page config ===
st.set_page_config(page_title="All-in-One Repair & Assistance", layout="centered")

# === Logo and Title ===
from PIL import Image
logo = Image.open("download.png")  # Make sure this file is in the same directory
st.image(logo, width=120)
st.title("🛠️ All-in-One Repair & Emergency Service")
st.markdown("Choose from a variety of services we offer across **home assistance** and **on-road emergencies.**")

# === Tabs for services ===
tab1, tab2 = st.tabs(["🏠 Home Services", "🚗 Highway Assistance"])

with tab1:
    st.subheader("🏠 Home Services")
    home_services = [
        "AC Repair", "Washing Machine Repair", "Refrigerator Repair",
        "TV Repair", "Fan Installation/Repair", "Plumbing", "Electrician",
        "Furniture Repair", "Door Lock Fix", "Painting", "Home Cleaning"
    ]
    selected_home_services = st.multiselect("Select services you need:", home_services)
    if selected_home_services:
        st.success(f"You have selected: {', '.join(selected_home_services)}")

with tab2:
    st.subheader("🚗 Highway Emergency Help")
    car_issues = [
        "Petrol/Diesel Finished", "EV Battery Discharged",
        "Flat Tyre / Air Inflation", "Towing Needed", "Engine Trouble"
    ]
    selected_issues = st.multiselect("Select the problem with your car:", car_issues)
    if selected_issues:
        st.success(f"Selected issues: {', '.join(selected_issues)}")

# === Contact Form ===
st.markdown("### 📞 Contact & Location Details")
name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
location = st.text_area("Your Address / Current Location")

if st.button("📩 Submit Request"):
    if name and phone and location:
        st.success("✅ Your request has been submitted! We'll reach out shortly.")
    else:
        st.warning("⚠️ Please fill all the details.")

st.markdown("---")
st.caption("Built with ❤️ in Python using Streamlit")
