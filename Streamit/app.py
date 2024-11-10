import streamlit as st
import numpy as np 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split



st.title("Welcome to Streamlit App!")
st.subheader("Data:")


@st.cache_data()
def dataset():
    df=pd.DataFrame(load_iris().data,columns=load_iris().feature_names)
    df["Species"]=load_iris().target
    labels=load_iris().target_names
    return df,labels
df,label=dataset()

x_train,x_test,y_train,y_test=train_test_split(df.iloc[:,:-1],df["Species"],random_state=123)


model=RandomForestClassifier()
model.fit(x_train,y_train)


st.sidebar.title("Lets Do the Predictions")
seple=st.sidebar.slider("sepal length (cm)",float(df["sepal length (cm)"].min()),float(df["sepal length (cm)"].max()))
sepwi=st.sidebar.slider("sepal width (cm)",float(df["sepal width (cm)"].min()),float(df["sepal width (cm)"].max()))
pele=st.sidebar.slider("petal length (cm)",float(df["petal length (cm)"].min()),float(df["petal length (cm)"].max()))
pelwi=st.sidebar.slider("petal width (cm)",float(df["petal width (cm)"].min()),float(df["petal width (cm)"].max()))

st.write(df)

st.subheader("Data Statistical info:")
st.write(df.describe())

st.subheader("Graphical Representation:")
st.bar_chart(df)


pre_data=[[seple,sepwi,pele,pelwi]]

predict=model.predict(pre_data)

result=label[predict[0]]

st.sidebar.write(f"Predicted Flower is:  {result}")



