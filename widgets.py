import streamlit as st
import pandas as pd 
st.title("streamlit text input ")
name=st.text_input('Enter Your Name :')
#age=st.text_input("Enter Your Age: ")
age=st.slider ("select your age :",0,100,25)


options=['Python','Java','dart','C']
Choice=st.selectbox("choose ur favourite language ",options)
st.write(f'you selected {Choice}')
st.write(f'Your age is :{age} ')
if name:
    st.write(f'hello,{name} ')
    
    # Create a DataFrame from a dictionary
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Score": [88, 79, 93, 85]
})
df.to_csv("deliveries.csv")
st.write(df)

 ## upload file 

uploaded_file=st.file_uploader('choose a csv file',type='csv')  
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)