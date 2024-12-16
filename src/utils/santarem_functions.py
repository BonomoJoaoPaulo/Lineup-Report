import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Força o uso do backend TkAgg para exibição interativa no tkinter
import matplotlib.pyplot as plt
from datetime import datetime

from utils.general_functions import get_most_recent_file
  
def compare_quantities_by_goods():
    directory = "../output/csv"
    file_prefix = "santarem_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    df["QUANTIDADE (T)"] = df["QUANTIDADE (T)"].str.replace(".", "").str.replace(",", ".")
    df["QUANTIDADE (T)"] = pd.to_numeric(df["QUANTIDADE (T)"], errors="coerce")

    mercadoria_totais = df.groupby("MERCADORIA")["QUANTIDADE (T)"].sum().sort_values()

    # Plotar
    plt.figure(figsize=(10, 6))
    mercadoria_totais.plot(kind="barh", color="skyblue")
    plt.title("Quantidades Totais por Tipo de Mercadoria")
    plt.xlabel("Quantidade (T)")
    plt.ylabel("Mercadoria")
    plt.tight_layout()
    plt.show()
