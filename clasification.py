import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache the dataset to speed up loading

def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load data
df, target_names = load_data()

# Train model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# App title
st.title("🌸 Iris Flower Classifier (with Sidebar)")

# Sidebar inputs
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal length (cm)", 0.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Sepal width (cm)", 0.0, 5.0, 3.5)
petal_length = st.sidebar.slider("Petal length (cm)", 0.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal width (cm)", 0.0, 3.0, 0.2)

# Sidebar prediction button
if st.sidebar.button("Predict"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)
    st.sidebar.success(f"🌼 Predicted Species: {target_names[prediction[0]]}")

# Main area
st.write("### 📊 Iris Dataset Preview")
st.dataframe(df.head())

# Feature importance visualization
st.write("### 🌿 Feature Importance")
feature_importances = pd.Series(model.feature_importances_, index=df.columns[:-1])
st.bar_chart(feature_importances)
