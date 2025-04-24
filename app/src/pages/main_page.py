import pandas as pd
import plotly.express as px
import streamlit as st
from src.main import df, get_data_agg
from src.utils.cards import create_cards
from src.utils.plotly_charts.bar_modified import plot_taxa_conversao_estado_civil
from src.utils.plotly_charts.histogram import histogram


def show_main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>
          Visão Geral
         </br> 
        </h1>   
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)

    with cols[0]:
        total_clientes = len(df)
        clientes_convertidos = df[df["Target"] == "yes"].shape[0]

        taxa_conversao = (clientes_convertidos / total_clientes) * 100
        create_cards("Taxa de Conversao (%)", f"{taxa_conversao:.2f}%")
    with cols[1]:
        create_cards(
            "Valor medio de saldo",
            f'{ get_data_agg(df=df, column_name="balance", agg_type="mean"):.2f}',
        )
    with cols[2]:
        create_cards(
            "Total de Clientes",
            get_data_agg(df=df, column_name="age", agg_type="count"),
        )

    col = st.columns(2)

    with col[0]:
        group = df["age"].value_counts().reset_index()
        histogram(
            df=group,
            x="age",
            y="count",
            title="Distribuicao por idade",
            log_y=True,
            color="blue",
            x_label="Idade",
            y_label="Quantidade",
        )
    with col[1]:

        plot_taxa_conversao_estado_civil(df, col[1], color="blue")


show_main()
