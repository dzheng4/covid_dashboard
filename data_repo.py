import numpy as np
import time
import numpy as np
import pandas as pd
import plotly.express as px

# Load Penn csv file
penn_retail_df = pd.read_csv('states_data\\PA\\Pennsylvania_Retail_Pharmacy_Vaccine_Allocation2022_06_23.csv', dtype = {
        'Retail Pharmacy Partner Name' : str,
        'Address 1' : str,
        'City' : str,
        'County' : str,
        'State' : str,
        'Zip Code' : str,
        'Vaccine' : str,
        'Date' : str,
        'Doses' : float,
        'Georeferenced Latitude & Longitude' : str
    },
    parse_dates = ['Date'],
    infer_datetime_format=True
)

# Load State link csv file
summary_df = pd.read_csv('states_data\\Official_State_COVID_LINKS.csv', dtype = {
        'State' : str,
        'Link' : str,
        'Data Score' : float,
        'Distribution' : str,
        'Provider' : str,
        'Wastage' : str
    }
)