import streamlit as st
from PIL import Image
import pandas as pd
from pathlib import Path


st.set_page_config(page_title='Project Files')
st.sidebar.success('Please select a page')

'#### Bodyfat dataset'

my_csv = Path (https://github.com/OktaySadakDA/bodyfat_estimator_app/blob/master/bodyfat.csv)
df = pd.read_csv(my_csv.resolve(), sep=',')
st.dataframe(df,width=1250)


@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download bodyfat data as CSV",
    data=csv,
    file_name='bodyfat.csv',
    mime='text/csv',
)

st.divider()

with st.expander('Context',expanded=False):
    st.write('''
        Lists estimates of the percentage of body fat determined by underwater
weighing and various body circumference measurements for 252 men.
             ''') 
with st.expander('Educational use of the dataset',expanded=False):
    st.write('''
        This data set can be used to illustrate multiple regression techniques. Accurate measurement of body fat is inconvenient/costly and it is desirable to have easy methods of estimating body fat that are not inconvenient/costly.
             ''')
with st.expander('Content',expanded=False):
    st.write('''
        The variables listed below are:
             
- Density determined from underwater weighing
- Percent body fat from Siri's (1956) equation
- Age (years)
- Weight (kg)
- Height (cm)
- Neck circumference (cm)
- Chest circumference (cm)
- Abdomen 2 circumference (cm)
- Hip circumference (cm)
- Thigh circumference (cm)
- Knee circumference (cm)
- Ankle circumference (cm)
- Biceps (extended) circumference (cm)
- Forearm circumference (cm)
- Wrist circumference (cm)
             
(Measurement standards are apparently those listed in Benhke and Wilmore (1974), pp. 45-48 where, for instance, the abdomen 2 circumference is measured "laterally, at the level of the iliac crests, and anteriorly, at the umbilicus".)

These data are used to produce the predictive equations for lean body weight given in the abstract "Generalized body composition prediction equation for men using simple measurement techniques", K.W. Penrose, A.G. Nelson, A.G. Fisher, FACSM, Human Performance Research Center, Brigham Young University, Provo, Utah 84602 as listed in Medicine and Science in Sports and Exercise, vol. 17, no. 2, April 1985, p. 189. (The predictive equation were obtained from the first 143 of the 252 cases that are listed below).
             ''')
with st.expander('More Details',expanded=False):
    st.write('''
        A variety of popular health books suggest that the readers assess their health, at least in part, by estimating their percentage of body fat. In Bailey (1994), for instance, the reader can estimate body fat from tables using their age and various skin-fold measurements obtained by using a caliper. Other texts give predictive equations for body fat using body circumference measurements (e.g. abdominal circumference) and/or skin-fold measurements. See, for instance, Behnke and Wilmore (1974), pp. 66-67; Wilmore (1976), p. 247; or Katch and McArdle (1977), pp. 120-132).

The percentage of body fat for an individual can be estimated once body density has been determined. Folks (e.g. Siri (1956)) assume that the body consists
of two components - lean body tissue and fat tissue. Letting:

D = Body Density (gm/cm^3)
A = proportion of lean body tissue
B = proportion of fat tissue (A+B=1)
a = density of lean body tissue (gm/cm^3)
b = density of fat tissue (gm/cm^3)
we have:

D = 1/[(A/a) + (B/b)]

solving for B we find:

B = (1/D)*[ab/(a-b)] - [b/(a-b)].

Using the estimates a=1.10 gm/cm^3 and b=0.90 gm/cm^3 (see Katch and McArdle (1977), p. 111 or Wilmore (1976), p. 123) we come up with "Siri's equation":

Percentage of Body Fat (i.e. 100*B) = 495/D - 450.

Volume, and hence body density, can be accurately measured a variety of ways. The technique of underwater weighing "computes body volume as the difference between body weight measured in air and weight measured during water submersion. In other words, body volume is equal to the loss of weight in
water with the appropriate temperature correction for the water's density" (Katch and McArdle (1977), p. 113). Using this technique,

Body Density = WA/[(WA-WW)/c.f. - LV]

where:

- WA = Weight in air (kg)
- WW = Weight in water (kg)
- c.f. = Water correction factor (=1 at 39.2 deg F as one-gram of water occupies exactly one cm^3 at this temperature, =.997 at 76-78 deg F)
- LV = Residual Lung Volume (liters)
             
(Katch and McArdle (1977), p. 115). Other methods of determining body volume are given in Behnke and Wilmore (1974), p. 22 ff.
             ''')
with st.expander('Source',expanded=False):
    st.write('''
        The data were generously supplied by Dr. A. Garth Fisher who gave permission to freely distribute the data and use for non-commercial purposes.

Roger W. Johnson
             
Department of Mathematics & Computer Science
             
South Dakota School of Mines & Technology
             
501 East St. Joseph Street
             
Rapid City, SD 57701

email address: rwjohnso@silver.sdsmt.edu
             
web address: http://silver.sdsmt.edu/~rwjohnso
             ''')         

