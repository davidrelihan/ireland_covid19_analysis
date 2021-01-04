import pandas as pd

def get_daily_c19_ireland_data():
    df = pd.read_excel("data/ireland_hospital_c19_stats.xlsx", sheet_name=0)

    #add rolling mean
    df["c19_icu_cases_rm"] = df["c19_icu_cases"].rolling(3).mean()
    df["c19_ventilated_cases_rm"] = df["c19_ventilated_cases"].rolling(3).mean()
    df["available_icu_beds_rm"] = df["available_icu_beds"].rolling(3).mean()

    #df = df[0:26]
    df = df.tail(360)
    return df

def get_c19_ireland_testing_dataset():
    df_hspc = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/f6d6332820ca466999dbd852f6ad4d5a_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")
    df_hspc['Date'] = pd.to_datetime(df_hspc['Date_HPSC']) # csv file date format was changed to milliseconds
    df_hspc['Datestr'] = df_hspc['Date'].dt.strftime('%d/%m')

    # Add daily Tests
    df_hspc["tests_new"] = df_hspc["TotalLabs"].diff().clip(0)
    df_hspc["tests_new_rm"] = df_hspc["tests_new"].rolling(3).mean()

    return df_hspc.tail(360)

def get_gov_c19_ireland_dataset():
    df_hspc = pd.read_csv("http://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}")
    df_hspc['Date'] = pd.to_datetime(df_hspc['Date']) # csv file date format was changed to milliseconds
    df_hspc['Datestr'] = df_hspc['Date'].dt.strftime('%d/%m')

    # add cases
    df_hspc["ConfirmedCovidCases_new"] = df_hspc["TotalConfirmedCovidCases"].diff().clip(0)
    df_hspc["ConfirmedCovidCases_new_rm"] = df_hspc["ConfirmedCovidCases_new"].rolling(3).mean()

    # add deaths
    df_hspc["ConfirmedCovidDeaths_rm"] = df_hspc["ConfirmedCovidDeaths"].rolling(3).mean()

    # add new hospital admissions
    df_hspc["HospitalisedCovidCases_new"] = df_hspc["HospitalisedCovidCases"].diff().clip(0)
    df_hspc["HospitalisedCovidCases_new_rm"] = df_hspc["HospitalisedCovidCases_new"].rolling(3).mean()
    df_hspc["HospitalisedCovidCases_new_7_rm"] = df_hspc["HospitalisedCovidCases_new"].rolling(7).mean()

    # add ICU
    df_hspc["RequiringICUCovidCases_new"] = df_hspc["RequiringICUCovidCases"].diff().clip(0)
    df_hspc["RequiringICUCovidCases_new_rm"] = df_hspc["RequiringICUCovidCases_new"].rolling(3).mean()

    HospitalisedAged5 = df_hspc["HospitalisedAged5"].diff().clip(0)
    df_hspc.insert(14, "HospitalisedAged5_new", HospitalisedAged5)
    df_hspc["HospitalisedAged5_new_rm"] = df_hspc["HospitalisedAged5_new"].rolling(3).mean()

    HospitalisedAged5to14 = df_hspc["HospitalisedAged5to14"].diff().clip(0)
    df_hspc.insert(16, "HospitalisedAged5to14_new", HospitalisedAged5to14)
    #add rolling mean
    df_hspc["HospitalisedAged5to14_new_rm"] = df_hspc["HospitalisedAged5to14_new"].rolling(3).mean()
    # HospitalisedAged15to24
    HospitalisedAged15to24 = df_hspc["HospitalisedAged15to24"].diff().clip(0)
    df_hspc.insert(18, "HospitalisedAged15to24_new", HospitalisedAged15to24)
    df_hspc["HospitalisedAged15to24_new_rm"] = df_hspc["HospitalisedAged15to24_new"].rolling(3).mean()
    # HospitalisedAged25to34
    HospitalisedAged25to34 = df_hspc["HospitalisedAged25to34"].diff().clip(0)
    df_hspc.insert(20, "HospitalisedAged25to34_new", HospitalisedAged25to34)
    df_hspc["HospitalisedAged25to34_new_rm"] = df_hspc["HospitalisedAged25to34_new"].rolling(3).mean()
    # HospitalisedAged35to44
    HospitalisedAged35to44 = df_hspc["HospitalisedAged35to44"].diff().clip(0)
    df_hspc.insert(22, "HospitalisedAged35to44_new", HospitalisedAged35to44)
    df_hspc["HospitalisedAged35to44_new_rm"] = df_hspc["HospitalisedAged35to44_new"].rolling(3).mean()
    # HospitalisedAged45to54
    HospitalisedAged45to54 = df_hspc["HospitalisedAged45to54"].diff().clip(0)
    df_hspc.insert(24, "HospitalisedAged45to54_new", HospitalisedAged45to54)
    df_hspc["HospitalisedAged45to54_new_rm"] = df_hspc["HospitalisedAged45to54_new"].rolling(3).mean()
    # HospitalisedAged55to64
    HospitalisedAged55to64 = df_hspc["HospitalisedAged55to64"].diff().clip(0)
    df_hspc.insert(26, "HospitalisedAged55to64_new", HospitalisedAged55to64)
    df_hspc["HospitalisedAged55to64_new_rm"] = df_hspc["HospitalisedAged55to64_new"].rolling(3).mean()
    # HospitalisedAged65up
    HospitalisedAged65up = df_hspc["HospitalisedAged65up"].diff().clip(0)
    df_hspc.insert(28, "HospitalisedAged65up_new", HospitalisedAged65up)
    df_hspc["HospitalisedAged65up_new_rm"] = df_hspc["HospitalisedAged65up_new"].rolling(3).mean()

    df_hspc = df_hspc.tail(360)
    return df_hspc
