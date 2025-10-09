# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st

load=open('LG.pkl','rb')
model=pickle.load(load)

def predict (Pclass,Age,SibSp,Parch,Sex_female,Sex_male,Embarked_C,Embarked_Q,Embarked_S,PassengerId,Fare):
    prediction = model.predict([[Pclass, Age, SibSp, Parch, Sex_female, Sex_male, Embarked_C, Embarked_Q, Embarked_S,PassengerId,Fare]])
    return prediction

def main():
    st.title('Titanic survival analysis')
    Pclass=st.number_input('Pclass: ')
    Age=st.number_input('Age: ')
    SibSp=st.number_input('SibSp: ')
    Parch=st.number_input('Parch: ')
    Sex_female=st.number_input('Sex_Female: ')
    Sex_male=st.number_input('Sex_male: ')
    Embarked_C=st.number_input('Embarked_C: ')
    Embarked_Q=st.number_input('Embarked_Q: ')
    Embarked_S=st.number_input('Embarked_S: ')
    PassengerID=st.number_input('PassengerID: ')
    Fare=st.number_input('Fare: ')
    
    
    if st.button('Predict'):
     result=predict(Pclass,Age,SibSp,Parch,Sex_female,Sex_male,Embarked_C,Embarked_Q,Embarked_S,PassengerID,Fare)
     if result==0:
         st.success('Not Survied')
     else:
         st.success('Survived')
         
         
if __name__=='__main__':
    main()