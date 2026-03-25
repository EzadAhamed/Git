import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("Iris.csv")


df.drop('Id', axis=1, inplace=True)

X = df.drop('Species', axis=1,errors = 'ignore')
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

import pickle

with open("classifier.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="🌸 Iris GUI", layout="centered")

st.markdown("""
<style> 

.stApp {
    background: linear-gradient(to right, black, maroon); 
} 

h1 { 
    text-align: center;     
    color: #6f42c1; 
} 

label { 
    font-weight: 600; 
    color: #333; 
} 
    
.stSlider > div > div > div > div { 
    background: linear-gradient(90deg, #6f42c1, #ff4b4b); 
} 
    
div.stButton > button { 
    background-color: #6f42c1; 
    color: white; border-radius: 10px; 
    padding: 10px 20px; 
    font-weight: bold; 
    border: none; 
} 
    
div.stButton > button:hover { 
    background-color: #5a32a3; 
} 
</style>
""", unsafe_allow_html=True)


st.title("🪻 Iris Species")


st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("Adjust the sliders to predict the species")

sepal_length = st.slider("Sepal Length (cm)", 0.0, 8.0, 4.0)
sepal_width = st.slider("Sepal Width (cm)", 0.0, 8.0, 2.0)
petal_length = st.slider("Petal Length (cm)", 0.0, 8.0, 3.0)
petal_width = st.slider("Petal Width (cm)", 0.0, 8.0, 1.0)

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Selected Values")
st.write(f"Sepal Length: {sepal_length} cm")
st.write(f"Sepal Width: {sepal_width} cm")
st.write(f"Petal Length: {petal_length} cm")
st.write(f"Petal Width: {petal_width} cm")

st.markdown('</div>', unsafe_allow_html=True)


if st.button("Predict"):

    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    st.write(f"Predicted Iris Species: {prediction[0]}")
