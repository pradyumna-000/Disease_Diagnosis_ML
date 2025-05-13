# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:43:53 2025

@author: pvtam
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/pvtam/OneDrive/Desktop/Coding/ML/Deployment/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/pvtam/OneDrive/Desktop/Coding/ML/Deployment/Heart_disease_prediction.sav', 'rb'))

parkinson_model = pickle.load(open('C:/Users/pvtam/OneDrive/Desktop/Coding/ML/Deployment/parkinson_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('C:/Users/pvtam/OneDrive/Desktop/Coding/ML/Deployment/breast_cancer_model.sav', 'rb'))
#sidebar for navigation

with st.sidebar:
    selected = option_menu(('Multiple Disease Prediction System'),
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction', 
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           icons=['activity', 'heart', 'person', 'person'],
                           default_index = 0)

#prediction page
if (selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction:')
    
    #getting input data from user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
    with col2:
        Glucose = st.number_input('Glucose Level')
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
    with col2:
        Insulin = st.number_input('Insulin Level')
    with col3:
        BMI = st.number_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.number_input('Age of the Person')
        
    #code for prediction
    diab_diagnosis = ''

    #creating a button for prediction
    if st.button('Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'Diabetic'
        else:
            diab_diagnosis = 'Non-Diabetic'
    st.success(diab_diagnosis)
    

if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction:')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex')
    with col3:
        cp = st.number_input('Chest Pain types')
    with col1:
        trestbps = st.number_input('Rest Blood Pressure')
    with col2:
        chol = st.number_input('Serum Cholestoral (mg/dl)')
    with col3:
        fbs = st.number_input('Fast Blood Sugar >120 mg/dl')
    with col1:
        restecg = st.number_input('Rest Electro-cardiographic results')
    with col2:
        thalach = st.number_input('Max Heart Rate achieved')
    with col3:
        exang = st.number_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.number_input('thal:-(0 = normal; 1 = fixed defect; 2 = reversable defect)')
           
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Positive'
        else:
          heart_diagnosis = 'Negative'
        
    st.success(heart_diagnosis)
    
    
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction:')
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.number_input('MDVP:RAP')
    with col2:
        PPQ = st.number_input('MDVP:PPQ')
    with col3:
        DDP = st.number_input('Jitter:DDP')
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')
    with col3:
        APQ = st.number_input('MDVP:APQ')
    with col4:
        DDA = st.number_input('Shimmer:DDA')
    with col5:
        NHR = st.number_input('NHR')
    with col1:
        HNR = st.number_input('HNR')
    with col2:
        RPDE = st.number_input('RPDE')
    with col3:
        DFA = st.number_input('DFA')
    with col4:
        spread1 = st.number_input('spread1')
    with col5:
        spread2 = st.number_input('spread2')
    with col1:
        D2 = st.number_input('D2')
    with col2:
        PPE = st.number_input('PPE')
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "Positive"
        else:
          parkinsons_diagnosis = "Negative"
        
    st.success(parkinsons_diagnosis)
    
if (selected == 'Breast Cancer Prediction'):
    #page title
    st.title('Breast Cancer Prediction:')
        
    #getting input data from user
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        mean_radius = st.number_input('Mean Radius')
    with col2:
        mean_texture = st.number_input('Mean Texture')
    with col3:
        mean_perimeter = st.number_input('Mean Perimeter')
    with col4:
        mean_area = st.number_input('Mean Area')
    with col5:
        mean_smoothness = st.number_input('Mean Smoothness')
    with col1:
        mean_compactness = st.number_input('Mean Compactness')
    with col2:
        mean_concavity = st.number_input('Mean Concavity')
    with col3:
        mean_concave_points = st.number_input('Mean Concave Points')
    with col4:
        mean_symmetry = st.number_input('Mean Symmetry')
    with col5:
        mean_fractal_dimension = st.number_input('Mean Fractal Dimension')
    with col1:
        radius_error = st.number_input('Radius Error')
    with col2:
        texture_error = st.number_input('Texture Error')
    with col3:
        perimeter_error = st.number_input('Perimeter Error')
    with col4:
        area_error = st.number_input('Area Error')
    with col5:
        smoothness_error = st.number_input('Smoothness Error')
    with col1:
        compactness_error = st.number_input('Compactness Error')
    with col2:
        concavity_error = st.number_input('Concavity Error')
    with col3:
        concave_points_error = st.number_input('Concave Points Error')
    with col4:
        symmetry_error = st.number_input('Symmetry Error')
    with col5:
        fractal_dimension_error = st.number_input('Fractal Dimension Error')
    with col1:
        worst_radius = st.number_input('Worst Radius')
    with col2:
        worst_texture = st.number_input('Worst Texture')
    with col3:
        worst_perimeter = st.number_input('Worst Perimeter')
    with col4:
        worst_area = st.number_input('Worst Area')
    with col5:
        worst_smoothness = st.number_input('Worst Smoothness')
    with col1:
        worst_compactness = st.number_input('Worst Compactness')
    with col2:
        worst_concavity = st.number_input('Worst Concavity')
    with col3:
        worst_concave_points = st.number_input('Worst Concave Points')
    with col4:
        worst_symmetry = st.number_input('Worst Symmetry')
    with col5:
        worst_fractal_dimension = st.number_input('Worst Fractal Dimension')
        
    #code for prediction
    breast_cancer_diagnosis = ''

    #creating a button for prediction
    if st.button('Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])
        
        if (breast_cancer_prediction[0] == 0):
            breast_cancer_diagnosis = 'Malignant'
        else:
            breast_cancer_diagnosis = 'Benign'
    st.success(breast_cancer_diagnosis)