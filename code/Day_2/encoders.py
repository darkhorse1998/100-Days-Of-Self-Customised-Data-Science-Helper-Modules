import pandas as pd
from tqdm import tqdm


def suggest_encoding(dfs):
    """

    Input: Pandas Series Data

    Output: Comments suggesting encoding and results

    """
    cats = dfs.unique()
    cats_count = dfs.nunique()
    total = dfs.shape[0]

    print(f"Total number of Entries : {total}")
    print(f"Number of Unique Entries : {cats_count}")
    print(f"Percentage of Unique Entries : {(cats_count/total)*100}")

    if (cats_count/total) > 0.90:
        print(f"Column --> {dfs} : Unique Values Percentage --> {round((cats_count/total)*100,2)}")
        prit("If it is a categorical column, better drop it.")

    if cats_count > 5 and dfs.dtypes not in [int, float]:
        print("Order of Preference of Encoding: ")
        print("1. Label Encoding --> Binary Encoding\n2. One Hot Encoding")

    if cats_count<5:
        print("Better to go for One Hot Encoding if xgboost is supposed to be applied")

def oneHotEncoding(df):
    """

    Input: Data Frame/ Slices of Data Frames
            Eg. df[["col1","col2"]]

    Output: Data Frame with the One Hot Encoded Columns

    """
    original_columns = list(df.columns)
    df = df.copy()

    for col in list(df.columns):

        for cat in list(df[col].value_counts().index):
            df[col + "_" + str(cat)] = 0
    for i in tqdm(range(df.shape[0])):
        for col in original_columns:
            df.loc[i, (str(col) + "_" + str(df.loc[i, col]))] = 1

    df.drop(original_columns, axis=1, inplace=True)

    return df
