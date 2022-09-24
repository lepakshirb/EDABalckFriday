import pandas as pd
from pandas_profiling import ProfileReport

#EDA using pandas-profiling
profile = ProfileReport(pd.read_csv('blackFriday_train.csv'), explorative=True)

#Saving results to a HTML file
profile.to_file("pandasprofiling_report.html")