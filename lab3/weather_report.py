import requests
import pandas as pd
import os



url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=23.8103&longitude=90.4125"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    "&timezone=Asia%2FDhaka&forecast_days=7"
)


res = requests.get(url)


print("Status code:", res.status_code)


res.raise_for_status()


weather = res.json()

print("Keys in response:", list(weather.keys()))




daily = weather["daily"]

df = pd.DataFrame({
    "date": daily["time"],
    "temperature_max_c": daily["temperature_2m_max"],
    "temperature_min_c": daily["temperature_2m_min"],
    "precipitation_mm": daily["precipitation_sum"]
})


print("\nFirst 5 days:")
print(df.head())




print("\nDataset info:")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Types:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())



df.to_csv("dhaka_weather.csv", index=False)

print("\nCSV saved:", os.path.exists("dhaka_weather.csv"))
