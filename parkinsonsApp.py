# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:41:46 2022

@author: Hamed
"""

#importing depndencies
import numpy as np
import pickle 
import streamlit as st


#loading saved model
path = r"C:/Users/Hamed/Desktop/parkinsonsDetection/trained_svmModel.sav"
loadModel = pickle.load(open(path, 'rb'))

#Creating prediction function
def parkinson_prediction(input_data):
    
    #Converting values to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #Reshaping the numpy array so it can predict for one data point
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    #Model prediction
    prediction = loadModel.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
      return "The person does not have Parkinsons Disease"
    
    else:
      return "This person has Parkinsons Disease"
  
    
def main():
    
    #title
    
    st.title('Parkinsons Detection Webiste')
    
    #input values
    
    MDVPFoHz = st.text_input('MDVP:Fo(Hz)')
    MDVPFhiHz = st.text_input('MDVP:Fhi(Hz)')
    MDVPFloHz = st.text_input('MDVP:Flo(Hz)')
    MDVPJitterPer = st.text_input('MDVP:Jitter(%)')
    MDVPJitterAbs = st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP = st.text_input('MDVP:RAP')
    MDVPPPQ = st.text_input('MDVP:PPQ')
    JitterDDP = st.text_input('Jitter:DDP')
    MDVPShimmer = st.text_input('MDVP:Shimmer')
    MDVPShimmerdB = st.text_input('MDVP:Shimmer(dB)')
    ShimmerAPQ3 = st.text_input('Shimmer:APQ3')
    ShimmerAPQ5 = st.text_input('Shimmer:APQ5')
    MDVPAPQ = st.text_input('MDVP:APQ')
    ShimmerDDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1	 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
    
    #prediction
    result = ''
    
    #button
    
    if st.button('Parkinsons Result'):
        result = parkinson_prediction([MDVPFoHz, MDVPFhiHz, MDVPFloHz,
                                       MDVPJitterPer, MDVPJitterAbs, MDVPRAP,
                                   MDVPPPQ, JitterDDP, MDVPShimmer, MDVPShimmerdB,
                                       ShimmerAPQ3, ShimmerAPQ5, MDVPAPQ, ShimmerDDA,
                                       NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])
    st.success(result)
    
    
    
#calling main function
if __name__ == '__main__':
    main()
