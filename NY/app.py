import pandas as pd #pip install pandas openpyxl
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="A última do Ano", page_icon=":smoking:", layout="wide")
st.title('A Última do Ano')

df = pd.read_excel(
    io='ano_novo.xlsx',
    engine='openpyxl',
    sheet_name=0,
    skiprows=1,
    usecols='A,B,F,I',
    nrows=12,
)

st.dataframe(df)



# ---- SIDEBAR ----
st.sidebar.header("Filtre aqui:")
fellas = st.sidebar.multiselect(
    "Os Fellas foram selecionados",
    options=df["Fellas"].unique(),
    default=df["Fellas"].unique()
)