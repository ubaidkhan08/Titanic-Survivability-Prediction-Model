import streamlit as st
from joblib import dump, load
import numpy as np
import pandas as pd

#log_model = load('university_admission.joblib')

def main():
    st.title("Titanic Passenger Survival Prediction Model")
    html_temp = """
    <div style="background-color:teal ;padding:20px">
    </div>
    """

    st.subheader('Enter Your Age')
    AGE = st.number_input()


    st.subheader('Enter Your Ticket Price in $')
    FARE = st.slider(0, 520)


    st.subheader('Choose Your Gender')
    S = st.radio(('Female','Male','Transgenger','Prefer not to say'))
    if S == 'Female':
        SEX = 1

    elif S == 'Male':
        SEX = 0

    elif S == 'Transgenger':
        SEX = 1.5

    elif S == 'Prefer not to say':
        SEX = 1.5



    st.subheader('Choose Passenger Class')
    C = st.radio(('1st','2nd','3rd'))

    if C == '1st':
        Pc = 1

    elif C == '2nd':
        Pc = 2

    elif C == '3rd':
        Pc = 3

    
    st.subheader('Choose Port of Boarding the Titanic')
    E = st.selectbox(('Cherbourg', 'Queenstown', 'Southampton'))
    if E == 'Cherbourg':
        EMB = 1

    elif E == 'Queenstown':
        EMB = 2 

    elif E == 'Southampton':
        EMB = 0 


    st.subheader('No. of Siblings/Spouses Aboard the Ship')
    SibSp = st.number_input()


    st.subheader('No. of Parents/Children Aboard the Ship')
    Parch = st.number_input()


    if st.button('Predict My Chances'):
        output= classify(gre,tofel,sepal_length, sepal_width, petal_length, petal_width,research)
        st.success('Your chance of admission is: {}%'.format(output))



def classify(AGE,FARE,SEX,Pc,EMB,SibSp,Parch):
    inputs=np.array([[AGE,FARE,SEX,Pc,EMB,SibSp,Parch]]).reshape(1,-1)


    XX.iloc[0] = [inputs]
    XX = scalerrr.fit_transform(XX)
    log_model.predict([XX[0]])

    log_model = load('university_admission.joblib')
    predictionn=log_model.predict([XX[0]])
    predd = '{}'.format(predictionn)
    return(float(predd[1:7])*100)

    #predictionn=log_model.predict(inputs)
    #predd = '{}'.format(predictionn)
    #return(float(predd[1:8])*100)


if __name__=='__main__':
    main()
