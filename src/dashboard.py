import pandas as pd
import streamlit as st
from pandas.core.common import not_none

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Análise de Lucro")
    uploaded_file = st.file_uploader("Coloque o seu arquivo aqui")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        with st.sidebar:
            distinct_country = df["MERCHANT_COUNTRY"].unique().tolist()
            city_selected = st.selectbox("País Específico", distinct_country)

            device_selected = st.radio("Dispositivo", ["MOBILE", "TABLET", "DESKTOP"], index=None)

            if city_selected:
                df = df[df["MERCHANT_COUNTRY"] == city_selected]

            if device_selected:
                df = df[df["DEVICE"] == device_selected]

st.write("Lucro por tipo de campanha")

st.bar_chart(df, x="CAMPAIGN_TYPE", y="TOTAL_PRICE")
st.dataframe(df, use_container_width=True)
