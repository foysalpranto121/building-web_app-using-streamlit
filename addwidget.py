import streamlit as st

st.title("Interactive Widgets Example")

# Slider
age = st.slider("Select your age", 0, 100, 18)
st.write(f"Your age is: {age}")

# Checkbox
if st.checkbox("Show details"):
    st.write("You checked the box!")

# Button
if st.button("Click me"):
    st.balloons()
