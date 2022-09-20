import pandas as pd
import math as m
import streamlit as st
import plotly.graph_objects as go

#from EMI import EMI, Amount, Loan, Years, fn
#c=pd.DataFrame()
#import streamlit_tags as stt

Amount = st.slider('Select Principal Amount in Thousands', 0,500,10,step=5)
#st.write("Loan amount:", Years)
Years=st.slider('Select Tenure Period in Months', 0,60,3,step=1)
Rate=st.slider('Select Rate of Interest', 0.0,10.0,5.0,step=0.25)
st.write("-----------------------")
Amount=Amount*100000
if Years > 3:
   #st.write(Years)
   MAmount = round(Amount * (pow((1 + (Rate) / 400), (Years*4/12))))
   st.info(MAmount)
else:
   MAmount = round(Amount * (pow((1 + (Rate) / 100), (Years/12))))
   st.write('Maturity Amount:',MAmount)
li=['Interest','Principal Amount']
n=[MAmount-Amount,Amount]
#n=[(a*100)/(CI+a),(CI*100)/(CI+a)]
fig = go.Figure(
go.Pie(
labels = li,
values = n,
hoverinfo = "label+percent",
textinfo = "value"
))
st.subheader("Distribution of Maturity Amount")
st.plotly_chart(fig)