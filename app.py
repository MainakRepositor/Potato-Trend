import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Load data
data = pd.read_csv("potato_yield.csv")

# Sidebar filters
year = st.sidebar.selectbox("Year", sorted(data["Year"].unique()))
state = st.sidebar.selectbox("State", sorted(data["State"].unique()))

# Filter data based on sidebar selections
filtered_data = data[(data["Year"] == year) & (data["State"] == state)]

# Display filtered data
st.write(f"Potato yield for {state} in {year}:")
st.write(filtered_data)

# Group data by month and calculate average yield
grouped_data = filtered_data.groupby("Month").mean().reset_index()

# Create Altair chart
chart = alt.Chart(grouped_data).mark_bar().encode(
    x="Month",
    y="Yield",
    tooltip=["Month", "Yield"]
).properties(
    title=f"Average Monthly Potato Yield for {state} in {year}"
)

# Display Altair chart
st.altair_chart(chart, use_container_width=True)

df = pd.read_csv('potato_yield.csv')

# Calculate total yield by summing the yield column
total_yield = df['Yield'].sum()

# Create a new DataFrame with the total yield for each state
yield_by_state = df.groupby('State')['Yield'].sum().reset_index()

# Create a pie chart using Plotly
fig = px.pie(yield_by_state, values='Yield', names='State', 
             title=f'Total Potato Yield by State: {total_yield}')

# Display the chart in Streamlit
st.plotly_chart(fig)

