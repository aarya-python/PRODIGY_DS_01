# -*- coding: utf-8 -*-
"""task1pynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QCvPDdRzzYriVIydFJ2EY5Qy15yOqKba
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with your actual file name)
df = pd.read_csv(r"/content/API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv", skiprows=4)

# Check available columns
print(df.columns)

# Let's plot total population for the year 2022 (if available)
df_pop = df[['Country Name', '2022']].dropna().sort_values(by='2022', ascending=False).head(10)

# Plot
plt.figure(figsize=(12,6))
plt.bar(df_pop['Country Name'], df_pop['2022'])
plt.title('Top 10 Countries by Population in 2022')
plt.ylabel('Population')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()