import pandas as pd

from merge_data import merge_data

# Laden der CSV-Dateien in Pandas DataFrames
players = ["Messi", "cristiano_ronaldo", "mbappe"]
player_df = pd.DataFrame()

data = merge_data(players, player_df)
#Todo: Clean up data for corrmatrixx
correlation_matrix = data.corr()



print()