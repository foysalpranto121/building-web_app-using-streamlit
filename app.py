import streamlit as st
import pandas as pd
import numpy as np

##  Tittle of the Application 
st.title('hello streamlit ')
## display a simple text
st.write(" This is a simple text ")

## create a simple DataFrame 
df=pd.DataFrame({

'first column':[1,2,3,4],
'second column':[10,20,30,40]


})
## display the dataframe
st.write("here is the data frame")
st.write(df)

st.title("📈 Student Progress Line Chart")

# --- Create progress data ---
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
scores = np.random.randint(50, 100, size=5)  # random scores between 50–100

data = pd.DataFrame({
    "Week": weeks,
    "Score": scores
})

# --- Show the data table ---
st.write("### Progress Data Table")
st.dataframe(data)

# --- Create the line chart ---
st.write("### 📊 Line Chart of Weekly Scores")
#st.line_chart(data.set_index("Week"))

st.line_chart(data)