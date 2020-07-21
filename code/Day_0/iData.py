import sys
import os
from tqdm import tqdm
import pandas as pd

if "tqdm" not in sys.modules:
    from tqdm import tqdm

if "os" not in sys.modules:
    import os

if "pandas" not in sys.modules:
    import pandas as pd


def import_all_from_directory(path):
    print("Loading files...")
    files = os.listdir(path=path)
    csv_files = []
    json_files = []
    excel_files = []
    dataframes = {}

    for f in files:
        if f.split(".")[-1] == "csv":
            csv_files.append(f)
        elif f.split(".")[-1] == "json":
            json_files.append(f)
        elif f.split(".")[-1] == "xlsx":
            excel_files.append(f)

    print("Creating Data Frames...")
    for f in tqdm(files):
        title = os.path.join(path,f.split(".")[0])
        if f in csv_files:
            dataframes[title] = pd.read_csv(title + ".csv")
        elif f in json_files:
            dataframes[title] = pd.read_json(title + ".json")
        elif f in excel_files:
            dataframes[title] = pd.read_excel(title + ".xlsx")
        else:
            print("File Not Appended")
    print("Data Frames Loaded")
    df_names = []
    for i in list(dataframes.keys()):
        df_names.append(dataframes[i])
    print("Imported {} Data Files".format(len(df_names)))
    print('File Headings:')
    for i in list(dataframes.keys()):
        print(i.split("\\")[-1], end=",")
    return df_names
