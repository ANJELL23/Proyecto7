import streamlit as st
import pandas as pd
import plotly.express as px

# Leer dataset
car_data = pd.read_csv('vehicles_us.csv') 

st.header("Análisis de Anuncios de Venta de Coches en USA")
st.write("Esta aplicación permite visualizar histogramas y gráficos de dispersión interactivos del dataset.\n\n Se puede explorar la información mediante:")

# Histograma
if st.checkbox('Mostrar histograma'):
    st.write('Histograma de la columna Odometro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión'):
    st.write('Gráfico de dispersión: Odimetro vs Precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)