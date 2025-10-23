import pandas as pd
import chardet

# Load dataset
def read_encoding(file_path):
    with open(file_path,'rb') as f:
        raw_data = f.read() 
        detect_data = chardet.detect(raw_data)
        encoding = detect_data['encoding'] 
        df = pd.read_csv(file_path, encoding = encoding)
        return df 
df = read_encoding('superstore.csv') 

# Check for missing values and data types
print(df.info())
print(df.isnull().sum())

# Fill missing values or drop rows
df = df.dropna(subset=['Order Date', 'Sales'])  # Adjust columns as needed

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Aggregate sales monthly
monthly_sales = df.groupby(pd.Grouper(key='Order Date', freq='ME')).agg({'Sales':'sum'}).reset_index()
monthly_sales.rename(columns={'Order Date':'ds', 'Sales':'y'}, inplace=True)
# Prophet needs columns 'ds' (datetime) and 'y' (target variable)

print(monthly_sales.head())
from prophet import Prophet

# Instantiate and fit the model
model = Prophet()
model.fit(monthly_sales)

# Forecast next 12 months
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

fig = model.plot(forecast)
model.plot_components(forecast)

# View forecasts
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))

# Export forecast to CSV for Power BI
export_df = forecast[['ds', 'yhat']]
export_df.rename(columns={'ds': 'Month', 'yhat': 'Forecasted Sales'}, inplace=True)
export_df.to_csv('superstore_forecast.csv', index=False)
# Region or category-based monthly sales for dashboard slicing
region_sales = df.groupby([pd.Grouper(key='Order Date', freq='ME'), 'Region'])['Sales'].sum().reset_index()
region_sales.rename(columns={'Order Date':'Month', 'Sales':'Region Sales'}, inplace=True)
region_sales.to_csv('region_sales_by_month.csv', index=False)

# Top items (for insight cards)
top_items = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).reset_index()
top_items.to_csv('top_items.csv', index=False)
