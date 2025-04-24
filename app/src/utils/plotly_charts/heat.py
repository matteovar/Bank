import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def heatmap(
    df: pd.DataFrame,
    title: str,
    x_title: str = "X Axis Title",
    y_title: str = "Y Axis Title",
    z_title: str = "Intensity",
    log_z: bool = False,
    color_continuous_scale: str = None,
):
    # Se for log, aplicar transformação nos dados (adiciona 1 para evitar log(0))
    z_data = np.log1p(df.values) if log_z else df.values

    heatmap_fig = px.imshow(
        z_data,
        x=df.columns,
        y=df.index,
        labels=dict(x=x_title, y=y_title, color=z_title),
        title=title,
        color_continuous_scale="Viridis",
    )

    st.plotly_chart(heatmap_fig)
