import pandas as pd #pip install pandas openpyxl
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
set.set_page_config(page_title="A última do Ano", page_icon=":smoking:", layout="wide")

df = pd.read_excel(
    io='ano_novo.xlsx',
    engine='openpyxl',
    sheet_name='NY',
    skiprows=3,
    usecols='B:R',
    nrows=12 
)

st.dataframe(df)
