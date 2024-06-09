import streamlit as  st 
import pandas as pd 
import numpy as np
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards

df = pd.read_csv("Online Sales Data.csv")


st.title(' AMRICAN ONLINE SALE EDA')
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

with st.expander('view datasheet'):
    st.dataframe(df.head(5)) 

# create kpi 

city_name = st.sidebar. multiselect('Selct CITY NAME',
options=df['Region'].unique(),
default=df['Region']. unique()[:3])

filtered_df = df[(df['Region'].isin(city_name))]



col1, col2, col3 = st.columns(3)
# Calculate key metrics
total_revenue = filtered_df['Total Revenue'].sum()
total_units_sold = filtered_df['Units Sold'].sum()
average_unit_price = filtered_df['Unit Price'].mean()

# Display key metrics using metric cards
st.info('TOTAL AMRICAN ONLINE SALE KPI', icon="📈")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Units Sold", f"{total_units_sold}")
col3.metric("Average Unit Price", f"${average_unit_price:,.2f}")
style_metric_cards(background_color='green')



# barh chart
product_count=filtered_df.groupby('Product Category')['Units Sold'].sum().reset_index()

st.info('TOTAL UNITS SALE BY PRODUCT', icon='📊',)
fig = px.pie(product_count, names ='Product Category', values='Units Sold',title='UNITS SOLD', hole=0.4)


st.plotly_chart(fig, use_container_width=True)

st.info('Dealer by Total Units', icon='📈') 
fig = px.line(filtered_df, x='Date', y='Units Sold', title='Line Chart')
st.plotly_chart(fig, use_container_width=True)

st.markdown(""" create by mahibul1234@gmail.com""")

st.info('Top-Selling Products by Units Sold', icon="📈")
top_products = filtered_df.groupby('Product Name')['Units Sold'].sum().reset_index()
top_products = top_products.sort_values(by='Units Sold', ascending=False).head(10)  # Top 10 products
fig = px.bar(top_products, x='Units Sold', y='Product Name', orientation='h')
st.plotly_chart(fig, use_container_width=True)
