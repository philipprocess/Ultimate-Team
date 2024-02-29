import pandas as pd
import matplotlib.pyplot as plt
from merge_data import merge_data

# Initialisierung einer Liste mit den Spielernamen,
# um sie automatisch aus dem Dateisystem einlesen zu können
players = ["Messi", "cristiano_ronaldo", "mbappe"]
#Initialisierung eines leeren Dataframes, in welches die Spielerdaten gespeichert werden
player_df = pd.DataFrame()

"""Startpunkt des Programms"""
if __name__ == "__main__":

    # Aufruf der Funktion, Daten in das passende Format für eine Korrelationsanalyse zusammenzuführen
    data = merge_data(players, player_df)

    # Erstellung der Korrelationsmatrix, wobei nur die Spalte "AveragePrice" interessant ist,
    # da die Korrelation von Spielern auf den Preis analysiert werden soll
    correlation_matrix = data.corr()
    correlation_matrix = correlation_matrix['AveragePrice']
    print("Korrelationen von Attributen auf den Preis als Tabelle:")
    print(correlation_matrix)



    """Erstellung eines Barchart-Plots für die Korrelationsmatrix"""
    ax = correlation_matrix.plot(kind='bar', figsize=(12, 10))

    """Hinzufügen der Zahlen für jeden Balken"""
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center',
                    va='center',
                    xytext=(0, 0),
                    textcoords='offset points')
    """Titel und Label setzen"""
    plt.title('Korrelationskoeffizienten zwischen Durchschnittspreis und Attributen')
    plt.ylabel("Korrelation")
    plt.show()
