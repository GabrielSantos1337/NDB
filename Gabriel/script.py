import pandas as pd
data_files = [
    "ap_2010.csvint",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for f in data_files:
    d = pd.read_csv("PY-EX\schools\{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

