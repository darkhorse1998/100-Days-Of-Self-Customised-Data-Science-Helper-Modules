import pandas as pd
import numpy as np

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

        print("Skew Type --> {}".format(skew_tye))
        print("Skewness --> {}".format(skewness))
        print("Comments --> {}".format(comment))

        pct_max_occur = list(df_col.value_counts(normalize=True))[0]
        max_occur = list(df_col.value_counts().index)[0]
        if pct_max_occur > 0.80:
            print(f"{df_col} :: Entry : {max_occur} --> {pct_max_occur*100}%")
        print("Standard Deviation of {} --> {}".format(df_col, df_col.values.std()))

    except Exception as e:
        print(e)
        print("This function takes a single Pandas Series column.")


def transform(df_col,details=False):

    """
    Input: df_col --> Pandas Series Data
           details --> Default : False, if True returns Details of all Transformations

    Output: Numpy Array containing the Transformed Data
    """

    p_skew_t = {
    0: lambda x: np.log(x),
    1: lambda x: np.sqrt(x),
    2: lambda x: np.cbrt(x)
    }

    n_skew_t = {
    0: lambda x: np.square(x),
    1: lambda x: np.cube(x)
    }

    diff = []

    try:
        initial_skew = df_col.skew()
        print("Initial Skewness --> ".format(initial_skew))
        if initial_skew > 0:

            Transformations = [
            "Logarithmic Transformation",
            "Square Root Transformation",
            "Cube Root Transformation"
            ]

            t_log_skew = np.log(df_col).skew()
            t_sqrt_skew = np.sqrt(df_col).skew()
            t_cbrt_skew = np.cbrt(df_col).skew()

            if t_log_skew < initial_skew and t_log_skew > 0:
                diff.append(initial_skew-t_log_skew)
            else:
                diff.append(float('-inf'))

            if t_sqrt_skew < initial_skew and t_sqrt_skew > 0:
                diff.append(initial_skew-t_sqrt_skew)
            else:
                diff.append(float('-inf'))

            if t_cbrt_skew < initial_skew and t_cbrt_skew > 0:
                diff.append(initial_skew-t_cbrt_skew)
            else:
                diff.append(float('-inf'))

            max_diff = max(diff)
            max_diff_index= np.argmax(diff)

            if details:
                print("Logarithmic Transformation Skewness --> {}".format(t_log_skew))
                print("Square Root Transformation Skewness --> {}".format(t_sqrt_skew))
                print("Cube Root Transformation Skewness --> {}".format(t_cbrt_skew))

            print("Transformation Completed...")
            print("Transformation Used --> {}".format(Transformations[max_diff_index]))
            print("Skewness improved by --> {}".format(max_diff))

            return p_skew_t[max_diff_index](df_col)

        elif initial_skew < 0:

            Transformations = [
            "Square Transformation",
            "Cube Transformation"
            ]

            t_sq_skew = np.square(df_col)
            t_cu_skew = np.cube(df_col)

            if t_sq_skew > initial_skew and t_log_skew < 0:
                diff.append(abs(initial_skew - t_sq_skew))
            else:
                diff.append(float('-inf'))

            if t_cu_skew > initial_skew and t_sqrt_skew < 0:
                diff.append(abs(initial_skew - t_cu_skew))
            else:
                diff.append(float('-inf'))

            max_diff = max(diff)
            max_diff_index= np.argmax(diff)

            if details:
                print("Square Transformation Skewness --> {}".format(t_sq_skew))
                print("Cube  Transformation Skewness --> {}".format(t_cu_skew))

            print("Transformation Completed...")
            print("Transformation Used --> {}".format(Transformations[max_diff_index]))
            print("Skewness improved by --> {}".format(max_diff))

            return n_skew_t[max_diff_index](df_col)

        else:
            diff.append(0)
            print("No Transformation Required.")


    except Exception as e:
        print(e)
        print("This function takes a single Pandas Series column.")
