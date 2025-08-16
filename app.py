import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('Social_Network_Ads.csv')
data = pd.get_dummies(data,drop_first=True,dtype=int)
data = data.rename(columns={'Gender_Male': 'Gender'})

X = data.drop(columns= ['User ID','Purchased'])
y = data['Purchased']

model = LogisticRegression(max_iter=1000)

model.fit(X.values,y)

st.title("Social Network  Ads Prediction")
st.write("Predict whether a person will purchase based on Age, Estimated Salary, and Gender.")

#inputs
age = st.number_input("Enter Age:",min_value=18,max_value=70,value=30)
salary = st.number_input("Enter the Salary:",min_value=10000,max_value=200000,value=10000)
gender = st.radio("Select Gender",("Male","Female"))

gender_value = 1 if gender == "Male" else 0

if st.button("Predict"):
    Predictions = model.predict([[age,salary,gender_value]])
    if Predictions[0] == 1:
        st.success("This Person is likely to purchase the product!")
    else:
        st.warning("This person is unlikely to purchase the product.")
            