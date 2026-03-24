import streamlit as st

st.set_page_config(page_title="🌸Iris GUI", layout="centered")


st.title("🪻 Iris Species")
st.write("Adjust the sliders to predict the species")


sepal_length = st.slider("Sepal Length (cm)", 0.0, 8.0)
sepal_width = st.slider("Sepal Width (cm)", 0.0, 8.0)
petal_length = st.slider("Petal Length (cm)", 0.0, 8.0)
petal_width = st.slider("Petal Width (cm)", 0.0, 8.0)


st.subheader("Selected Values")
st.write(f"Sepal Length: {sepal_length} cm")
st.write(f"Sepal Width: {sepal_width} cm")
st.write(f"Petal Length: {petal_length} cm")
st.write(f"Petal Width: {petal_width} cm")


st.button("Predict Species")
    