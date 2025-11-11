
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import ggplot, aes, geom_point, labs, theme_minimal


file_path = r"C:\Users\rajso\OneDrive\Desktop\archive\DataScience_salaries_2024.csv"
DataScience_salaries_2024 = pd.read_csv(file_path)

print("----- HEAD -----")
print(DataScience_salaries_2024.head())

print("\n----- INFO -----")
print(DataScience_salaries_2024.info())

print("\n----- SUMMARY -----")
print(DataScience_salaries_2024.describe(include='all'))

missing_values = DataScience_salaries_2024.isna().sum().sum()
print(f"\nCount of total missing values: {missing_values}")

duplicates = DataScience_salaries_2024.duplicated().sum()
print(f"Count of total duplicate observations: {duplicates}")

print("\nColumn Names:")
print(DataScience_salaries_2024.columns.tolist())

plt.figure(figsize=(6,4))
sns.histplot(DataScience_salaries_2024['salary'], kde=True, bins=30)
plt.title("Histogram of Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(DataScience_salaries_2024['salary_in_usd'], kde=True, bins=30)
plt.title("Histogram of Salary (in USD)")
plt.xlabel("Salary in USD")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(DataScience_salaries_2024['remote_ratio'], kde=False, bins=10)
plt.title("Histogram of Remote Ratio")
plt.xlabel("Remote Ratio")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(
    data=DataScience_salaries_2024,
    x='salary_in_usd',
    y='salary',
    cmap='viridis'
)
plt.title("2D Histogram: Salary vs Salary in USD")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=DataScience_salaries_2024['salary'])
plt.title("Boxplot of Salary")
plt.show()


plt.figure(figsize=(6,4))
sns.scatterplot(x='salary_in_usd', y='salary', data=DataScience_salaries_2024)
plt.title("Scatter Plot: Salary vs Salary in USD")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='remote_ratio', y='salary', data=DataScience_salaries_2024)
plt.title("Boxplot of Salary by Remote Ratio")
plt.show()

sns.lmplot(
    x='salary_in_usd',
    y='salary',
    hue='remote_ratio',
    data=DataScience_salaries_2024,
    fit_reg=False,
    palette='Set2',
    height=5,
    aspect=1.2
)
plt.title("Scatter Plot by Remote Ratio")
plt.show()

plt.figure(figsize=(8,5))
DataScience_salaries_2024['salary'].value_counts().head(20).plot(kind='bar')
plt.title("Top 20 Salary Frequency")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.kdeplot(x=DataScience_salaries_2024['salary'], fill=True, color='teal')
plt.title("Density Plot of Salary")
plt.xlabel("Salary")
plt.show()


plot = (
    ggplot(DataScience_salaries_2024, aes(x='salary', y='salary_in_usd')) +
    geom_point(color='blue', alpha=0.6) +
    labs(title='Salary vs Salary in USD',
         x='Salary',
         y='Salary in USD') +
    theme_minimal()
)
print(plot)

