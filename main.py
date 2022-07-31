from common import bar_graph_plotter
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

# Employee Specific analysis

# Determining Employees seeking treatment of their mental illness in US
bar_graph_plotter('state', 'treatment', 'count', 'Employees seeking treatment of their mental illness in US')

# Determining Employees seeking treatment of their mental illness in World
bar_graph_plotter('country', 'treatment', 'count', 'Employees seeking treatment of their mental illness in World')

# Determining Employees knowing options for mental care their employer provides in US
bar_graph_plotter('state', 'care_options', 'count', 'Employees knowing options for mental care their employer provides in US')

# Determining Employees knowing options for mental care their employer provides in World
bar_graph_plotter('country', 'care_options', 'count', 'Employees knowing options for mental care their employer provides in World')

# Determining Employees comfortable discussing their mental health with their coworkers in US
bar_graph_plotter('state', 'coworkers', 'count', 'Employees comfortable discussing their mental health with their coworkers in US')

# Determining Employees comfortable discussing their mental health with their coworkers in World
bar_graph_plotter('country', 'coworkers', 'count', 'Employees comfortable discussing their mental health with their coworkers in World')

# Determining Employees comfortable discussing their mental health with their direct supervisor in US
bar_graph_plotter('state', 'supervisor', 'count', 'Employees comfortable discussing their mental health with their direct supervisor in US')

# Determining Employees comfortable discussing their mental health with their direct supervisor in World
bar_graph_plotter('country', 'coworkers', 'count', 'Employees comfortable discussing their mental health with their direct supervisor in World')

# Determining Employers who put mental health as important as physical health as per employee
bar_graph_plotter('state', 'mental_vs_physical', 'count', 'Employers who put mental health as important as physical health as per employee')

# Determining Employers who put mental health as important as physical health as per employee
bar_graph_plotter('country', 'mental_vs_physical', 'count', 'Employers who put mental health as important as physical health as per employee')
