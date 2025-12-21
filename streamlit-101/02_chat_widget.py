# Import packages
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import altair as alt
import os
from dotenv import load_dotenv,find_dotenv
from openai import OpenAI
load_dotenv(find_dotenv())


# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configure page
st.set_page_config(page_title="Add chat widget", layout="wide")

# Title
st.title("Connect to OpenAI API")

# Load data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names) # Create dataframe
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names) # Add target variable

# Add sidebar filter
st.sidebar.header("Scatter plot filter options")

# Add species filter 
species_options = st.sidebar.multiselect("Select species", options=iris.target_names, default=list(iris.target_names))

# Allow user to change x-axis
x_axis = st.sidebar.selectbox("X-axix feature :", options=iris.feature_names, index=0)

# Allow user to change y-axis
y_axis = st.sidebar.selectbox("Y-axix feature :", options=iris.feature_names, index=1)

# Add chat widget in sidebar
st.sidebar.header("Chat widget")

#Determine if chat history exists in the session state and initialize if it doesn't
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
#Create text input field in sidebar to allow users to type in message
user_input = st.sidebar.text_input("Type a message ...", key="ui_input")

#Check if send button is clicked
if st.sidebar.button("Send", key="ui_send"):
     #Provide warning if user has not entered any input
    if not user_input.strip():
         st.warning("Please enter a message")
    #Add chat history in session state is the user has entered input
    else:
        #Add user's message to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        try:
            #Send chat history to OpenAI LLM and receive response
            response = client.chat.completions.create(
                #Select model
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
                )
            # Get assistant's response
            reply = response.choices[0].message.content
            # Add AI assistant's reply to chat history
            st.session_state.chat_history.append(f"Bot: {reply}")
        except Exception as e:
            #Handle API errors and add to chat history
            st.session_state.chat_history.append(f"Bot Error: {e}")
        
st.subheader("Chat window")
#Loop through the chat history stored in session state and display each message
for message in st.session_state.chat_history:
    st.write(message)
    
# Filter dataframe
filtered_df = df[df["species"].isin(species_options)]

# Create scatter plot
st.subheader("Scatter plot")
scatter = (alt.Chart(filtered_df).mark_circle(size=60).encode(x=x_axis, y=y_axis, color="species", tooltip=iris.feature_names + ["species"]).interactive())
st.altair_chart(scatter, width="stretch")

# Display filtered data
st.subheader("Filtered data")
st.dataframe(filtered_df)

# Display stats summary
st.subheader("Descriptive statistics summary")
st.write(filtered_df.describe())

# Add dashboard footer
st.write("---")
st.write("Dashboard built with streamlit and altair")