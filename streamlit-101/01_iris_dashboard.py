# simple dashboard with Iris dataset

# Import packages
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import altair as alt

# Configure page
st.set_page_config(page_title="Iris Dashboard", layout="wide")

# Title
st.title("Iris dataset dashboard")

# Load data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names) # Create dataframe
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names) # Add target variable

# Add sidebar filter
st.sidebar.header("Filter options for the scatter plot")

# Add species filter 
species_options = st.sidebar.multiselect("Select species", options=iris.target_names, default=list(iris.target_names))

# Allow user to change x-axis
x_axis = st.sidebar.selectbox("X-axix feature :", options=iris.feature_names, index=0)

# Allow user to change y-axis
y_axis = st.sidebar.selectbox("Y-axix feature :", options=iris.feature_names, index=1)

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