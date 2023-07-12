import pandas as pd
from datetime import datetime




def read_google_sheet(sheet_id = None):
    """
    Function to read in a google sheet as csv file using pandas. 
    Ensure that the sharing setting for the sheet allows anyone with the link to access it.

    Parameters
    ----------
    sheet_id : str, optional
        id of the google sheet extracted from the webpage as */d/sheet_id/edit*, by default None

    Returns
    -------
    DF : pandas dataframe
        Pandas dataframe containing information on google sheet
    """
    prefix = "https://docs.google.com/spreadsheets/d/"
    if sheet_id is None: sheet_id = "1riOck-CL8RjVkt_dgcgWhd0DWhUWMifpyb6VLngTrHs"
    
    DF = pd.read_csv(prefix+ sheet_id+ "/gviz/tq?tqx=out:csv")
    DF = DF.drop(columns= "Timestamp")

    #convert day-time string into date_time object
    format_string = "%m/%d/%Y %H:%M:%S"
    DF["date_time_of_airport_arrival"]  = [datetime.strptime(tt, format_string) for tt in DF["date_time_of_airport_arrival"] ]
    DF["date_time_of_hotel_departure"]  = [datetime.strptime(tt, format_string) for tt in DF["date_time_of_hotel_departure"] ]

    return DF
