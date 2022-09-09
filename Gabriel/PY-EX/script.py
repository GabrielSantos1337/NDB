import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

print(data["sat_results"].head())

for k in data:
    print(data[k].head())

all_survey = pd.read_csv("schools/survey_all.txt", delimiter = "\t", encoding = 'windows-1252')
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter = "\t", encoding = 'windows-1252')
survey = pd.concat([all_survey, d75_survey], axis=0)

print(survey.head())

survey["DBN"] = survey["dbn"]

survey_fields = [
    "DBN",
    "rr_s",
    "rr_t",
    "rr_p",
    "N_s",
    "N_t",
    "N_p",
    "saf_p_ll",
    "com_p_ll",
    "eng_p_ll",
    "aca_p_ll",
    "saf_t_ll",
    "com_t_ll",
    "eng_t_ll",
    "aca_t_ll",
    "saf_s_ll",
    "com_s_ll",
    "eng_s_ll",
    "aca_s_ll",
    "saf_tot_ll",
    "com_tot_ll",
    "eng_tot_ll",
    "aca_tot_ll",
]
survey = survey.loc[:,survey_fields]
data["survey"] = survey

print(survey.head())
