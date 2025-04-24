import pandas as pd

df = pd.read_csv("app/data/input/bank-full.csv")
df.rename(
    columns={
        "age": "Idade",
        "job": "Trabalho",
        "marital": "Estado civil",
        "education": "Educacao",
        "default": "Credito",
        "balance": "Balanco",
        "housing": "Imovel",
        "loan": "Emprestimo",
        "contact": "Contato",
        "day": "Dia",
        "month": "Mes",
        "duration": "Duracao",
        "campaign": "Entrou em contato",
        "pdays": "Dias passados",
        "previous": "Antes do Contato",
        "poutcome": "Campanha passada",
        "Target": "Deposito",
    },
    inplace=True,
)


def get_data_agg(df: pd.DataFrame, column_name: str, agg_type: str = None):
    return df[column_name].agg(agg_type)


def get_group_agg(
    df: pd.DataFrame, group_col: str, agg_col: str, agg_type: str = None
) -> pd.DataFrame:
    if agg_type is None:
        return df[
            [group_col, agg_col]
        ].drop_duplicates()  # Remove duplicatas para mostrar uma vez por data
    else:
        return df.groupby(group_col)[agg_col].agg(agg_type).reset_index()
