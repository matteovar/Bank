<<<<<<< HEAD
import plotly.express as px
=======
import pandas as pd
>>>>>>> bb82bc26f88c96543d1fb9558c0fd9485a89b7cd
import streamlit as st
from src.main import df
from src.utils.plotly_charts.bar import bar


def conv_camp(df):
    taxa_conversao = (
        df.groupby("Campanha passada")["Deposito"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .reset_index()
    )
    taxa_conversao["conversao"] = taxa_conversao["yes"] * 100
    bar(
        df=taxa_conversao,
        x="Campanha passada",
        y="conversao",
        x_label="Campanhas",
        y_label="Taxa de Conversao (%)",
        title="Taxa de Conversão por Resultado da Campanha Anterior",
        log_y=True,
        color_sequence=["#0000ff"],  # <- lista com uma_
    )


def conv_conta(df):
    taxa_conversao = (
        df.groupby("Contato")["Deposito"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .reset_index()
    )
    taxa_conversao["conversao"] = taxa_conversao["yes"] * 100
    bar(
        df=taxa_conversao,
        x="Contato",
        y="conversao",
        x_label="Campanhas",
        y_label="Taxa de Conversao (%)",
        title="Taxa de Conversão por tipos de comunicacao",
        log_y=True,
        color_sequence=["#0000ff"],  # <- lista com uma_
    )


def campanha():
    st.markdown(
        """
            <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Campanhas
            </h1>
    
            """,
        unsafe_allow_html=True,
    )

    col = st.columns(2)
    with col[0]:
        conv_camp(df)
    with col[1]:
        conv_conta(df)


campanha()
