import pandas as pd
import plotly.express as px
import streamlit as st


def scatter(
    df: pd.DataFrame,
    x: str,
    y,
    color=None,
    hover_name=None,
    hover_data=None,  # <- novo parâmetro
    size=None,
    title: str = "Gráfico",
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
    hover_label: str = None,
    log_y: bool = False,
    color_sequence=None,
):
    # Verifica se y é múltiplo (lista)
    if isinstance(y, list):
        df_long = df.melt(
            id_vars=[x], value_vars=y, var_name="Tipo", value_name="Valor"
        )
        y = "Valor"
        color = "Tipo"

        labels = {
            x: x_label if x_label else x,
            y: y_label if y_label else "Valor",
            color: color_label if color_label else "Tipo",
        }
        data_to_use = df_long
    else:
        labels = {x: x_label if x_label else x, y: y_label if y_label else y}
        if color and color_label:
            labels[color] = color_label
        data_to_use = df

    if hover_name and hover_label:
        labels[hover_name] = hover_label

    scatter_view = px.scatter(
        data_frame=data_to_use,
        x=x,
        y=y,
        color=color,
        hover_name=hover_name,
        hover_data=hover_data,  # <- incluído aqui
        size=size,
        title=title,
        labels=labels,
        log_y=log_y,
        color_discrete_sequence=color_sequence,
    )

    st.plotly_chart(scatter_view)
