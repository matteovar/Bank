
import pandas as pd
import seaborn as sns
import streamlit as st
from src.main import df
from src.utils.plotly_charts.bar import bar


def conv_camp(df):
    taxa_conversao = (
        df.groupby("poutcome")["Target"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .reset_index()
    )
    taxa_conversao["conversao"] = taxa_conversao["yes"] * 100
    st.dataframe(df)
    bar(
        df=taxa_conversao,
        x="poutcome",
        y="conversao",
        x_label="Campanhas",
        y_label="Taxa de Conversao (%)",
        title="Taxa de Conversão por Resultado da Campanha Anterior",
        log_y=True,
    )


def campanha():
    conv_camp(df)
    st.markdown(
        """
            <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Campanhas
            </h1>
    
            """,
        unsafe_allow_html=True,
    )

    taxa_conversao = (
        df.groupby("contact")["Target"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .reset_index()
    )
    taxa_conversao["conversao"] = taxa_conversao["yes"] * 100
    bar(
        df=taxa_conversao,
        x="contact",
        y="conversao",
        x_label="Campanhas",
        y_label="Taxa de Conversao (%)",
        title="Taxa de Conversão por tipos de comunicacao",
        log_y=True,
    )


campanha()
