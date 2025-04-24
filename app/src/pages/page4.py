import pandas as pd
import plotly.express as px
import streamlit as st
from src.main import df
from src.utils.plotly_charts.heat import heatmap
from src.utils.plotly_charts.scatter import scatter


def correlation(df):
    df_num = df[
        [
            "Idade",
            "Balanco",
            "Duracao",
            "Entrou em contato",
            "Dias passados",
            "Antes do Contato",
        ]
    ]
    correlation_matrix = df_num.corr()
    heatmap(
        correlation_matrix,
        title="Mapa de Correlação entre Variáveis Numérica",
        x_title="Variaveis",
        y_title="Variaveis",
        z_title="Correlacao",
        color_continuous_scale="RdBu_r",
    )


def advanced():
    st.markdown(
        """
            <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Insights Avançados
            </h1>
    
            """,
        unsafe_allow_html=True,
    )

    correlation(df)

    scatter(
        df=df,
        x="Idade",
        y="Balanco",
        color="Deposito",
        title="Dispersão: Idade x Saldo Bancário por Conversão",
        hover_data=["Educacao", "Trabalho"],
        log_y=True,
    )


advanced()
