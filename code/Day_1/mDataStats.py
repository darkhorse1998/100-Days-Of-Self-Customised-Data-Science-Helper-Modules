import pandas as pd


def conv_to_float(df=None):
    """
        Converts columns pf DataFrame to float, else appends errors to error_log keys
        :param df: -> DataFrame
        :return Dictionary of error logs:
    """

    error_log = {}
    for col in list(df.columns):
        error_log[col] = []
        for i in range(df[col].shape[0]):
            try:
                df.loc[i, col] = float(df.loc[i, col])
            except Exception as e:
                if e not in error_log[col]:
                    error_log[col].append(e)
        if not error_log[col]:
            error_log[col].append("No Errors")
            df[col] = df[col].astype("float64")
            print(f"{col} successfully converted to float")
        else:
            print(f"{col} couldn't be converted to float. Please check error logs")
    return error_log


def data_filling_option(df):
    """
    Gives stats on ffill and bfill
    :param df:
    :return: Different stats of the numerical and non-numerical data.
    """
    cols = df.columns.to_list()
    results = []
    difference = []
    df = df.dropna()
    df.reset_index(drop=True)

    for col in range(len(cols)):
        ffill = 0
        bfill = 0

        for i in range(1, df.shape[0] - 1):
            last_ = df.iloc[i - 1, col]
            next_ = df.iloc[i + 1, col]
            present_ = df.iloc[i, col]

            if present_ == last_:
                ffill += 1
            if present_ == next_:
                bfill += 1

        diff = ffill - bfill
        if diff > 0:
            results.append("ffill")
        elif diff < 0:
            results.append("bfill")
        else:
            results.append("equal")

        difference.append(abs(diff))

    stats = pd.DataFrame()
    stats['Filling_Method'] = results
    stats['Difference'] = difference

    return stats


class DataStats:

    def __init__(self):
        self.df = None

    def dstats(self, df):
        self.df = df
        col = list(self.df.columns)

        num_col = self.df.select_dtypes(include='number')
        non_num_col = self.df.select_dtypes(exclude='number')

        out_non_num = pd.DataFrame()
        out_num = pd.DataFrame()

        majority_non_col = []
        missing_values = []
        for c in list(non_num_col.columns):
            majority_non_col.append(list(non_num_col[c].value_counts())[0])
            missing_values.append(non_num_col[c].isna().sum())
        out_non_num['Columns'] = list(non_num_col.columns)
        out_non_num['Major Element'] = majority_non_col
        out_non_num['Missing Values'] = missing_values
        out_non_num = pd.concat([out_non_num, data_filling_option(non_num_col)], axis=1)

        out_num['Columns'] = list(num_col.columns)
        out_num['Mean'] = list(num_col.mean().values)
        out_num['Median'] = list(num_col.median().values)
        out_num['Skew'] = list(num_col.skew())

        return out_num, out_non_num
