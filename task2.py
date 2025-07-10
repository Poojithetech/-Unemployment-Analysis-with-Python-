import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and parse the ' Date' column
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv", parse_dates=[' Date'])

# Clean up column names
df.rename(columns={
    ' Date': 'Date',
    ' Estimated Unemployment Rate (%)': 'UnemploymentRate',
    'Region': 'State'
}, inplace=True)

# Drop missing values if any
df.dropna(subset=['UnemploymentRate'], inplace=True)

# Extract year and month for analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# --- 1. Line plot: National unemployment trend ---
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x='Date', y='UnemploymentRate', ci=None)
plt.axvspan(pd.to_datetime('2020-03-01'), pd.to_datetime('2020-11-30'), color='red', alpha=0.2, label='COVID-19 Period')
plt.title('India Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 2. State-wise trends ---
plt.figure(figsize=(14, 8))
sns.lineplot(data=df, x='Date', y='UnemploymentRate', hue='State', legend=False)
plt.title('State-wise Unemployment Trends')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 3. Monthly unemployment patterns ---
plt.figure(figsize=(10, 5))
sns.boxplot(x='Month', y='UnemploymentRate', data=df)
plt.title('Monthly Pattern in Unemployment Rate')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 4. COVID impact analysis ---
covid_df = df[(df['Date'] >= '2020-03-01') & (df['Date'] <= '2020-11-30')]
pre_covid_df = df[df['Date'] < '2020-03-01']

print("\nAverage Unemployment Rate Before COVID-19:", round(pre_covid_df['UnemploymentRate'].mean(), 2))
print("Average During COVID-19:", round(covid_df['UnemploymentRate'].mean(), 2))

# --- 5. Yearly average bar chart ---
yearly_avg = df.groupby('Year')['UnemploymentRate'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x='Year', y='UnemploymentRate', data=yearly_avg, palette="viridis")
plt.title('Average Unemployment Rate per Year')
plt.ylabel('Unemployment Rate (%)')
plt.xlabel('Year')
plt.grid(True)
plt.tight_layout()
plt.show()
