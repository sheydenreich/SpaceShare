import pandas as pd




def read_google_sheet(sheet_id = None):
    prefix = "https://docs.google.com/spreadsheets/d/"
    if sheet_id is None: sheet_id = "10aSO3AtjG69PFmjaLTmPm_vEPAAWiZsjmswgIDa6bGY"
    
    DF = pd.read_csv(prefix+ sheet_id+ "/gviz/tq?tqx=out:csv")
    DF = DF.rename(columns={'Preferred_departure_time  (allow for +/– 15 minutes )': 'Preferred_departure_time' })
    DF = DF.drop(columns= "Timestamp")

    return DF