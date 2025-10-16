import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Display Example")

# Create a DataFrame
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)
st.write("### Data Table:")
st.dataframe(data)

# Line chart
st.line_chart(data)

