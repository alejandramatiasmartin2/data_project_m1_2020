import pandas as pd

# Cleaning the data

def clean_gender(data_merged):

    # Standarization of the Gender column (Female/Male)
    data_merged['gender'].unique()
    data_merged['gender'] = data_merged['gender'].str.lower()
    data_merged.loc[(data_merged['gender'].str.lower().str[0] == 'm'), 'gender'] = 'Male'
    data_merged.loc[(data_merged['gender'].str.lower().str[0] == 'f'), 'gender'] = 'Female'
    print('Gender column cleaned')
    return data_merged