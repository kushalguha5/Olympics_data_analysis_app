import pandas as pd



def preprocess(df,region_df):
    #global df,region_df
    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    #merge with region df
    df = df.merge(region_df, on='NOC', how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #One hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    df = df.loc[:, ~df.columns.duplicated()]
    return df