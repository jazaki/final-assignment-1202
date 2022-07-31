from employee_analysis import run_employee_analysis
from employer_analysis import run_employer_analysis

# Import appropriate libraries to perform data analytics and visualization

import numpy as np
import pandas as pd
import plotly.express as px


# import and read the provided dataset using pandas

df = pd.read_csv('survey.csv')

# Return the first 5 rows for performing a quick test of the right type of data in our df object
df.head()

# Print a concise summary of the dataframe
df.info()

# Convert all columns to lowercase so as to reduce case sensistive mistakes in code
df.columns = df.columns.str.lower()

# Find out which country has the most number of participants in the survey
df['country'].value_counts()

# Find out the states that are unique in our dataframe
df['state'].unique()

# drop the unnecessary columns
df = df.drop(['timestamp','comments'], axis = 1)

# Generate a descriptive statistics of our dataframe analyzing both numeric and object series
df.describe(include='all')

# Run Employee Specific analysis
run_employee_analysis()

# Run Employee Specific analysis
run_employer_analysis()

