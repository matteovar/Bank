import pandas as pd
import streamlit as st
from src.main import df
from src.utils.plotly_charts.bar import bar


def taxa_meses(df):

    df["Mes"] = pd.Categorical(
        df["Mes"],
        categories=[
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        ],
        ordered=True,
    )

    taxa_conversao_estado_civil = (
        df.groupby("Mes")["Deposito"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .reset_index()
    )

    taxa_conversao_estado_civil["conversao"] = taxa_conversao_estado_civil["yes"] * 100
    top5 = (
        taxa_conversao_estado_civil.groupby("Mes")["conversao"]
        .sum()
        .reset_index()
        .sort_values("conversao", ascending=False)
    ).head(5)

    return top5


def taxa_dias_meses(df):
    taxa_conversao_estado_civil_1 = (
        df.groupby(["Dia", "Mes"])["Deposito"]
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .reset_index()
    )
    taxa_conversao_estado_civil_1["conversao"] = (
        taxa_conversao_estado_civil_1["yes"] * 100
    )
    selecione = st.multiselect(
        "Seleciona os meses",
        options=taxa_conversao_estado_civil_1["Mes"].unique(),
        default="jan",
    )

    df_filtered = taxa_conversao_estado_civil_1[
        taxa_conversao_estado_civil_1["Mes"].isin(selecione)
    ]
    bar(
        df=df_filtered,
        x="Dia",
        y="conversao",
        color="Mes",
        y_label="Taxa de Conversao (%)",
        x_label="Dias",
        log_y=True,
        title="Taxa de conversao em dias de acordo com os meses",
        color_sequence=["#0000ff"],  # <- lista com uma_
    )


def show_table(title, df, column, ascending=True):
    top10 = df.nsmallest(10, column) if ascending else df.nlargest(10, column)
    max_value = float(top10[column].max())  # <-- Aqui o fix

    st.markdown(f"#### {title}")
    st.dataframe(
        top10,
        column_order=("month", column),
        hide_index=True,
        width=None,
        column_config={
            "month": st.column_config.TextColumn("Meses"),
            column: st.column_config.ProgressColumn(
                column,
                format="%f",
                min_value=0,
                max_value=max_value,
            ),
        },
    )


def tendencias():
    st.markdown(
        """
            <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Tendências Temporais
            </h1>
    
            """,
        unsafe_allow_html=True,
    )

    taxa_dias_meses(df)

    top5 = taxa_meses(df)
    cols = st.columns(2)
    with cols[0]:
        taxa_meses(df)
        show_table(
            "Top 5 meses com maiores taxas de conversao",
            df=top5,
            column="conversao",
            ascending=False,
        )


tendencias()
