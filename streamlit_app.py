import streamlit as st
st.title("Retail Business Dashboard") 
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")
sales_target = st.number_input("Enter Monthly Sales Target (in USD):", min_value=0, value=50000)
region = st.selectbox("Select Region:", ["North", "South", "East", "West"])
if st.button("Submit"):
  st.write(f"Sales Target: ${sales_target}")
  st.write(f"Region Selected: {region}")
  st.success("Dashboard updated successfully!")
if sales_target > 100000:
  st.write("Great! You have set an ambitious target!")
