import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit.components.v1 import html


def histogram(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = None,
    log_y: bool = False,
    color: str = None,
    x_label: str = None,
    y_label: str = None,
):
    default_color = "blue"
    bar_color = color if color else default_color
    labels = {x: x_label if x_label else x, y: y_label if y_label else y}

    fig = px.histogram(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        color_discrete_sequence=[bar_color],
        labels=labels,
    )

    fig.update_layout(
        yaxis_type="log" if log_y else "linear",
        yaxis_title=y_label if y_label else y,  # Esta linha resolve o problema
    )

    fig.update_traces(
        marker_line_width=0.5,
        marker_line_color="white",
    )

    plot_html = fig.to_html(full_html=False, include_plotlyjs="cdn")

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
