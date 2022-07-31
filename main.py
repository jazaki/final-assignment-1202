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