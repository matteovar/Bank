import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit.components.v1 import html


def bar(
    df: pd.DataFrame,
    x: str,
    y,
    title: str = "Gráfico",
    color=None,
    orientation="v",
    graph_color: str = None,  # <- ainda pode usar se quiser uma cor única
    color_sequence=None,  # <- novo parâmetro
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
    barmode: str = None,
    log_y: bool = False,
):
    if isinstance(y, list):
        df = df.melt(
            id_vars=[x], value_vars=y, var_name="Categoria", value_name="Valor"
        )
        y = "Valor"
        color = "Categoria"

    labels = {x: x_label if x_label else x, y: y_label if y_label else y}
    if color and color_label:
        labels[color] = color_label

    bar_view = px.bar(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        color=color,
        orientation=orientation,
        labels=labels,
        barmode=barmode,
        color_discrete_sequence=color_sequence,  # <- aplica sequência personalizada
    )

    # Aplica log no eixo Y, se necessário
    bar_view.update_layout(yaxis_type="log" if log_y else "linear")

    # Caso queira aplicar cor única diretamente (quando não tem `color`)
    if not color and graph_color:
        bar_view.update_traces(marker_color=graph_color)

    plot_html = bar_view.to_html(full_html=False, include_plotlyjs="cdn")

    hist_html = f"""
    <style>
        .hist {{
            border: 1px solid #000;
            border-radius: 12px;
            padding: 15px;
            margin: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>
    <div class="hist">
        {plot_html}
    </div>
    """

    html(hist_html, height=500)
