
import numpy as np
import pandas as pd
def rm_main():
    names_col = [f'col{i+1}' for i in range(20)]
    market_data = pd.read_csv('market_data.csv', header=None, names=names_col)
    market_data = market_data.fillna(value='nan')
    numpay_market_data = market_data.to_numpy()

    # assume you have a 2D numpy array named "numpay_market_data" containing NaN values
    transcations_market = []
    for transaction in numpay_market_data :
      # create a boolean mask marking the NaN values as True and non-NaN values as False
      # print(transaction)
      mask = transaction!= 'nan'
      # filter the array by selecting only the non-NaN values
      clear_transation = transaction[mask]
      transcations_market.append(clear_transation)
    # print the resulting filtered array

    list_of_item = []

    for transaction in transcations_market:
        for item in transaction:
            if item not in list_of_item:
                list_of_item.append(item)

    # print(list_of_item)

    data = {}
    for item in list_of_item:
        data[item] = []
    for item in list_of_item:
        for transaction in transcations_market:
            if item in transaction:
                data[item].append(1)
            else :
                data[item].append(0)

    #load data into a DataFrame object:
    df = pd.DataFrame(data)
    df.to_csv('market_data_clean.csv', index=False)
# print(df)


