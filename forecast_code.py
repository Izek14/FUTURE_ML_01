import pandas as pd
import chardet
from prophet import Prophet
import holidays

def read_encoding(file_path):
    with open(file_path,'rb') as f:
        raw_data = f.read() 
        detect_data = chardet.detect(raw_data)
        encoding = detect_data['encoding'] 
        df = pd.read_csv(file_path, encoding = encoding)
        return df 
df = read_encoding('superstore.csv') 

print(df.info())
print(df.isnull().sum())

df = df.dropna(subset=['Order Date', 'Sales'])
df['Order Date'] = pd.to_datetime(df['Order Date'])

monthly_sales = df.groupby(pd.Grouper(key='Order Date', freq='ME')).agg({'Sales':'sum'}).reset_index()
monthly_sales.rename(columns={'Order Date':'ds', 'Sales':'y'}, inplace=True)
print(monthly_sales.head())

model = Prophet()
model.add_country_holidays(country_name='US')
model.fit(monthly_sales)

years = df['Order Date'].dt.year.unique()
us_holidays = holidays.US(years=years)
holiday_table = pd.DataFrame(
    {'Order Date': pd.to_datetime(list(us_holidays.keys())), 'holiday': list(us_holidays.values())}
)

sales_holidays = df.merge(holiday_table, on='Order Date', how='inner')
sales_holidays[['Order Date', 'Sales', 'holiday']].to_csv('holiday_sales.csv', index=False)

future = model.make_future_dataframe(periods=12, freq='ME')
forecast = model.predict(future)

fig = model.plot(forecast)
model.plot_components(forecast)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))

export_df = forecast[['ds', 'yhat', 'yhat_upper', 'yhat_lower']]
export_df = export_df.rename(columns={
    'ds': 'Month',
    'yhat': 'Forecasted Sales',
    'yhat_upper': 'Forecasted Sales Upper',
    'yhat_lower': 'Forecasted Sales Lower'
})
export_df.to_csv('superstore_forecast.csv', index=False)