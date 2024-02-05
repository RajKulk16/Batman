import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('online_retail_II.csv')

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("profile_report.html")