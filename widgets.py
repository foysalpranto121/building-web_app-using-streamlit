import streamlit as st
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
    
    
   