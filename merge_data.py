import pandas as pd

def merge_data(players, player_df):
    """Zwei for-Schleifen, die für das automatische Einlesen der csv Dateien sind.
        Erst werden die Fifa Teile iteriert von Fifa 20-24, anschließend die übergebenen Spieler in der Liste"""
    for i in range(20, 25, 1):
        for player in players:
            # Einlesen der Preise der Spieler
            prices_path = player + '/Prices/' + player + '_' + str(i) + '.csv'
            prices_df = pd.read_csv(prices_path, sep=';')

            """Hinzufügen des Namen des Spielers"""
            prices_df['Name'] = player

            """Einlesen der Attributdateien der Spieler"""
            attributes_path = player + '/Stats/' + player + '_fifa' + str(i) + '_real_gold_card_attributes.csv'
            attributes_df = pd.read_csv(attributes_path)

            """Zusammenführen der Preise mit Attributen"""
            merged_df = pd.merge(attributes_df, prices_df)

            """Berechnung des Durchschnittspreises der Spieler über die Märkte(Konsolen(XBOX,PS) und PC).
            Da ab Fifa23 die Märkte der Konsolen zusammengeführt wurden, 
            gibt es ab diesem Fifa nur noch die Preise für die Konsolen(Cross) und PC, weshalb dieses try-except
            beide Fälle behandelt, falls es noch keinen Cross Konsolenmarkt in manchen Daten gibt"""
            try:
                merged_df['AveragePrice'] = merged_df[['Cross', 'PC']].mean(axis=1)
            except KeyError:
                merged_df['AveragePrice'] = merged_df[['XBOX', 'PS', 'PC']].mean(axis=1)

            """Berechnung des Durchschnittes pro Spiel"""
            average_df = merged_df.groupby(['Name'])['AveragePrice'].mean()

            """Entfernen der Preise pro Markt"""
            try:
                merged_df.drop(columns=['AveragePrice', 'Cross', 'PC'], inplace=True)
            except KeyError:
                merged_df.drop(columns=['AveragePrice', 'XBOX', 'PS', 'PC'], inplace=True)

            """Hinzufügen des Durchschnittspreises an die erste Zeile, da lediglich die Attribute der Karte  einmal gebraucht werden"""
            merged_df = pd.merge(merged_df.iloc[:1], average_df, how='right', on='Name')

            """Sammeln der Spielerdaten"""
            player_df = pd.concat([player_df, merged_df], ignore_index=True)

    """Entfernen von unnötigen, oder nicht vollständigen Daten"""
    player_df.drop(columns=['Unnamed: 0', 'DateTime', 'Def. Awareness', 'Marking', 'Composure'], inplace=True)
    player_df.drop(columns=["Name", 'Game'], inplace=True)

    return player_df