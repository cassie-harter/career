# -*- coding: utf-8 -*-
"""prophet_forecast_monthly.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IYprMwsaI-wvWW2O9Sit-gzdbqJRfl6y
"""

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

df_data = pd.read_csv('/net_hires_prophet-model_20230807.csv')

from prophet import Prophet

model = Prophet()
model.fit(df_data)

future_periods = 12  # or any desired number of future periods
future = model.make_future_dataframe(periods=future_periods, freq='MS')
forecast = model.predict(future)

fig = model.plot(forecast)
plt.show()

fig2 = model.plot_components(forecast)

from prophet.plot import plot_plotly, plot_components_plotly

plot_plotly(model, forecast)

# Create a dataframe of the results
df_results = pd.DataFrame(model.predict())

df_results.head()

df_results.to_csv('/content/drive/MyDrive/All The Things/Career/NBCU/prophet_df_output_monthly.csv', index=False)
