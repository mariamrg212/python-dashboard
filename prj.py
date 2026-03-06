import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

#loading data
df=pd.read_csv("sales_data_sample.csv")

p1,p2,p3,p4=st.columns(4)
sales=int(df["SALES"].sum()/1000)
avg_price=int(df["PRICEEACH"].mean())
p1.metric("Total Sales",sales,border=True)
p2.metric("Max Qnt",df["QUANTITYORDERED"].max(),border=True)
p3.metric("Total Qnt",df["QUANTITYORDERED"].sum(),border=True)
#fig=px.pie(data_frame=df,names="DEALSIZE",values="QUANTITYORDERED",hole=.6)
#p3.plotly_chart(fig,use_container_width=True)
p4.metric("AVG Price",avg_price,border=True)


st.sidebar.title("Sales Dashboard")
st.sidebar.image("sale.jfif")
st.sidebar.write("this dashboard for discussing sales insights")
filter_1=st.sidebar.selectbox("Cat filter",[None,"STATUS","COUNTRY","PRODUCTLINE"])
filter_2=st.sidebar.selectbox("Num Filter",[None,"SALES","PRICEEACH"])

order=st.sidebar.slider("OrderNumber",1,18)

fig1=px.scatter(data_frame=df,x="PRICEEACH",y="QUANTITYORDERED",color=filter_1,size=filter_2)
st.plotly_chart(fig1,use_container_width=True)


c1,c2=st.columns((7,3))

with c1:
    st.title("Quntity vs sales")
    fig2=px.bar(data_frame=df,x="QTR_ID",y="SALES",text_auto=True,color=filter_1)
    st.plotly_chart(fig2,use_container_width=True)
with c2:
    fig3=px.pie(data_frame=df,names="DEALSIZE",values="QUANTITYORDERED")
    st.plotly_chart(fig3,use_container_width=True)