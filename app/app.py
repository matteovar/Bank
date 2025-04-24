import pandas as pd
import streamlit as st

st.set_page_config(page_title="Bank", layout="wide")


def main():

    pages_1 = {
        "Análise de Performance de Campanha ": [
            st.Page("src/pages/main_page.py", title="Visão Geral"),
            st.Page("src/pages/page_2.py", title="Tendências Temporais"),
            st.Page("src/pages/page3.py", title="Performance de Campanha"),
            st.Page("src/pages/page4.py", title="Insights Avançados"),
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
