import streamlit as st
import pandas as pd

# Set page title
st.title("📂 CSV File Uploader App")

# Short description
st.write("Upload a CSV file to preview its contents 👇")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display file info
    st.subheader("✅ File successfully uploaded!")
    st.write(f"**File Name:** {uploaded_file.name}")
    
    # Show dataframe
    st.subheader("📊 Data Preview:")
    st.dataframe(df.head())
    
    # Show basic data info
    st.subheader("ℹ️ Data Summary:")
    st.write(df.describe())
    
else:
    st.warning("Please upload a CSV file to continue.")
