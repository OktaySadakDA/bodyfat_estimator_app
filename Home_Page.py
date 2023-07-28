
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Home Page', page_icon='🏠')
st.sidebar.success('Please select a page')

'         # FIT & HOT Body Fat Estimator'

image = Image.open('image.jpeg')

st.image(image)

st.subheader('')


st.caption('')

import pickle
import numpy as np

with open('bodyfatmodel1.pkl', 'rb') as file:
    data = pickle.load(file)

# Access the loaded data
print(data)

def predict_note_authentication(Density,Abdomen,Chest,Weight,Hip):
    prediction = data.predict([[Density,Abdomen,Chest,Weight,Hip]])
    print(prediction)
    return float(prediction)

st.divider() 

'### Please enter below details to estimate your body fat.'

def main():
    #st.title("Please enter below details to estimate your body fat.")

    density= st.text_input('Enter Density','Type Here')
    abdomen= st.text_input('Enter Abdomen Circumference (in cm)','Type Here')
    chest= st.text_input('Enter Chest Circumference (in cm)','Type Here')
    weight= st.text_input('Enter Weight (in kg)','Type Here')
    hip= st.text_input('Enter Hip Circumference (in cm)','Type Here')

    result=''
    if st.button('Predict'):
        result = f'Your body fat percentage is :  {round(predict_note_authentication(density,abdomen,chest,weight,hip),2)} %'


    st.success(format(result))

    st.caption('''
        For example :
               
           - Enter Density : 1.0708
               
           - Enter Abdomen Circumference (in cm): 85.2
               
           - Enter Chest Circumference (in cm): 93.1
               
           - Enter Weight (in kg): 70.11	
               
           - Enter Hip Circumference (in cm): 94.5
               
           ''')
    
    if st.button('About'):
        st.text('Let\'s learn')
        st.text('Built by streamlit')

if __name__ == '__main__':
    main()




