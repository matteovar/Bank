import pandas as pd
import plotly.express as px
from streamlit.components.v1 import html


def plot_taxa_conversao_estado_civil(df, col, color: str = "#4C78A8"):
    """
    Plota gráfico de taxa de conversão por estado civil em um container estilizado

    Parâmetros:
    - df: DataFrame com os dados
    - col: Coluna do Streamlit onde o gráfico será renderizado
    - color: Cor das barras (padrão: '#4C78A8' - azul escuro)
    """
    with col:
        # Processamento dos dados
        taxa_conversao_estado_civil = (
            df.groupby("marital")["Target"]
            .value_counts(normalize=True)
            .unstack()
            .fillna(0)
        )
        taxa_conversao_estado_civil["conversao"] = (
            taxa_conversao_estado_civil["yes"] * 100
        )

        # Criação do gráfico
        fig = px.bar(
            taxa_conversao_estado_civil["conversao"],
            labels={
                "index": "Estado Civil",
                "value": "Taxa de Conversão (%)",
            },
            title="Taxa de Conversão por Estado Civil",
            color_discrete_sequence=[color],  # Nova linha para definir a cor
        )

        # Melhorias no gráfico
        fig.update_layout(
            xaxis_title="Estado Civil",
            yaxis_title="Taxa de Conversão (%)",
            yaxis_ticksuffix="%",
            plot_bgcolor="rgba(0,0,0,0)",  # Fundo transparente
            paper_bgcolor="rgba(0,0,0,0)",  # Fundo do gráfico transparente
        )

        fig.update_traces(
            hovertemplate="Estado Civil: %{x}<br>Taxa de Conversão: %{y:.1f}%<extra></extra>",
            marker_color=color,  # Garante a cor mesmo se não usar color_discrete_sequence
            marker_line_color="white",  # Borda branca nas barras
            marker_line_width=1.5,  # Espessura da borda
            opacity=0.9,  # Transparência leve
        )

        # Converter para HTML
        plot_html = fig.to_html(full_html=False, include_plotlyjs="cdn")

        # Container estilizado
        hist_html = f"""
        <style>
            .hist-conversao {{
                border: 1px solid #000;
                border-radius: 12px;
                padding: 15px;
                margin: 15px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
        </style>
        <div class="hist-conversao">
            {plot_html}
        </div>
        """

        html(hist_html, height=550)
