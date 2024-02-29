import pandas as pd

def merge_data(players, player_df):
    for i in range(20, 25, 1):
        for player in players:
            prices_path = player + '/Prices/' + player + '_' + str(i) + '.csv'
            prices_df = pd.read_csv(player + '/Prices/' + player + '_' + str(i) + '.csv', sep=';', parse_dates=['DateTime'])
            prices_df['Name'] = player
            attributes_path = player + '/Stats/' + player + '_fifa' + str(i) + '_real_gold_card_attributes.csv'
            attributes_df = pd.read_csv(attributes_path)

            merged_df = pd.merge(attributes_df, prices_df)

            try:
                merged_df['AveragePrice'] = merged_df[['Cross', 'PC']].mean(axis=1)
            except KeyError:
                merged_df['AveragePrice'] = merged_df[['XBOX', 'PS', 'PC']].mean(axis=1)

            average_df = merged_df.groupby(['Name'])['AveragePrice'].mean()
            try:
                merged_df.drop(columns=['AveragePrice', 'Cross', 'PC'], inplace=True)
            except KeyError:
                merged_df.drop(columns=['AveragePrice', 'XBOX', 'PS', 'PC'], inplace=True)

            merged_df = pd.merge(merged_df.iloc[:1], average_df, how='right', on='Name')

            player_df = pd.concat([player_df, merged_df], ignore_index=True)



    return player_df