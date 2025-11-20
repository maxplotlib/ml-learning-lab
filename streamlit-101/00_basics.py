# Import packages
import streamlit as st
from datetime import datetime

# Configure page
st.set_page_config(page_title="Streamlit Basics", layout="wide")

# Write title and text
st.title("Basic layout and widgets")
st.write("Hello World 😊")

# Get current date and time
st.write("Current ", datetime.now().strftime("Date : %d-%m-%Y, Time : %H:%M:%S"))

# Create a button
if st.button("Press here"):
    st.success("Button was pressed ✅")
    
# Create a slider 
age = st.slider("Select your age", 18, 100, 18)
st.write(f"You are {age} years old.")

# Create text input
name = st.text_input("Enter your name :")
st.write(f"Your name is {name}")

# Create checkbox
toggle = st.checkbox("Check for a surprise")
if toggle:
    st.info("Surprise! 🎉")

# Create multiselect
options = st.multiselect("Choose pizza toppings 🍕", ["Cheese 🧀", "Pepperoni 🌶️", "Olives 🫒"])
st.write("Toppings", options)

# Create sidebar
st.sidebar.title("Sidebar panel")
# Add options selection to sidebar
sidebar_options = st.sidebar.selectbox("Select an option", ["Home", "Settings", "About"])
st.sidebar.write(f"You selected :", sidebar_options)

# Create columns containers
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", "72°F", "-1.2°F")
with col2:
    st.metric("Wind Speed", "10 mph", "+1.5 mph")
with col3:
    st.metric("Humidity", "50%", "-5%")
    
# Create expender container
with st.expander("See more details"):
    st.write("More informations here ...")