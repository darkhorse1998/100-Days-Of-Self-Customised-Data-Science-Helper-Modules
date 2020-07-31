import pandas as pd

def skew_stats(df_col):
    """
        Input: Pandas Series Data format (single column)
        Output: void type
        Prints: skew_tye, skewness, comment
    """



    try:
        skew = df_col.skew()
        if skew>0:
            if skew <= 0.5:
                skew_tye = 'Approximately Normal'
                skewness = skew
                comment = "Can be considered as Normal Distribution"
            elif skew < 1:
                skew_tye = 'Positive'
                skewness = skew
                comment = "Moderately Skewed"
            else:
                skew_tye = 'Positive'
                skewness = skew
                comment = "Highly Skewed"

        elif skew<0:
            if skew >= -0.5:
                skew_tye = 'Approximately Normal'
                skewness = skew
                comment = "Can be considered as Normal Distribution"
            elif skew > -1:
                skew_tye = 'Negative'
                skewness = skew
                comment = "Moderately Skewed"
            else:
                skew_tye = 'Negative'
                skewness = skew
                comment = "Highly Skewed"
        else:
            skew_tye = 'Normal'
            skewness = skew
            comment = "Perfect Normal Distribution"

        print("Skew Type: {}".format(skew_tye))
        print("Skewness: {}".format(skewness))
        print("Comments: {}".format(comment))
    except Exception as e:
        print(e)
        print("This function takes a single Pandas Series column.")
