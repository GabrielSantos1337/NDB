import pandas as pd #pip install pandas openpyxl
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="A última do Ano", page_icon=":smoking:", layout="wide")
st.title('A Última do Ano')

df1 = pd.read_excel(
    io='ano_novo.xlsx',
    engine='openpyxl',
    sheet_name=0,
    skiprows=1,
    usecols='A:B',
    nrows=13,
)

df2 = pd.read_excel(
    io='ano_novo.xlsx',
    engine='openpyxl',
    sheet_name=0,
    skiprows=19,
    usecols='A:B',
    nrows=5,
)


#f2 = pd.DataFrame({'Data': ["Comida", "Bebida", "Nargas"], 'Custo': ["", "", ""]})

#df = pd.concat([df1, df2])
st.dataframe(df1)
st.dataframe(df2)

# ---- SIDEBAR ----
st.sidebar.header("Filtre aqui:")
fellas = st.sidebar.multiselect(
    "Os Fellas foram selecionados",
    options=df1["Fellas"].unique(),
    default=df1["Fellas"].unique()
)

custo = st.sidebar.selectbox(
    "Qual o Custo você deseja ver?",
    ("Comida", "Bebida", "Nargas")
)

df_selection1 = df1.query(
    "Fellas == @fellas"
)
df_selection2 = df2.query(
    "Custo == @custo"
)

df_selection = pd.concat([df_selection1, df_selection2])
st.dataframe(df_selection)

# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard de Controle")
st.markdown("##")

# TOP KPI's
#total_pago = int(df_selection1["Total"].sum())
valor = round(df_selection2["Valor"])
#custo = str(df_selection2["Custo"])
#star = ":star:" * int(round(pagou, 0))
#average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
   st.subheader("Total Pago:")
#   st.subheader(f"R$ {total_pago:,}")
with middle_column:
  st.subheader("Valor:")
  st.subheader(f"{custo}: R$ {valor}")
#with right_column:
#  st.subheader("Average Sales per Transaction:")
#   st.subheader(f"RS ${average_sale_by_transaction}")

st.markdown("---")
