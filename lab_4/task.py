import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://huggingface.co/datasets/SIH/palmer-penguins/resolve/main/penguins.csv"

# 1.
df = pd.read_csv(url)
print("FIRST 5 ROWS")
print(df.head())

# 2. 
print(" SHAPE")
print(df.shape)
print("DTYPES")
print(df.dtypes)
print(" INFO")
df.info()
print(" DESCRIBE")
print(df.describe())
print(" SPECIES COUNT")
print(df["species"].value_counts())

# 3. 
missing_counts = df.isna().sum()
missing_percent = df.isna().mean() * 100
rows_with_missing = df[df.isna().any(axis=1)]

print("MISSING COUNTS")
print(missing_counts)
print(" MISSING % ")
print(missing_percent.round(2))
print("ROWS WITH MISSING")
print(rows_with_missing.head())

# 4. 
body_mass = df["body_mass_g"].dropna()
mean_mass = np.mean(body_mass)
median_mass = np.median(body_mass)

print("BODY MASS STATS")
print("Mean:", mean_mass, "| Median:", median_mass)
print("Min:", body_mass.min(), "| Max:", body_mass.max())
print("Std:", np.std(body_mass, ddof=1))
print("Quartiles:", np.percentile(body_mass, [25, 50, 75]))
print("5 smallest:", body_mass.nsmallest(5).tolist())
print("5 largest :", body_mass.nlargest(5).tolist())

# 5. 
mass_values = df["body_mass_g"].dropna()
plt.figure(figsize=(8, 4))
plt.hist(mass_values, bins=15)
plt.xlabel("Body mass (g)")
plt.ylabel("Frequency")
plt.title("Distribution of Penguin Body Mass")
plt.tight_layout()
plt.show() 

# 6. 
plot_data = df[["flipper_length_mm", "body_mass_g"]].dropna()
plt.figure(figsize=(8, 4))
plt.scatter(plot_data["flipper_length_mm"], plot_data["body_mass_g"], alpha=0.7)
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.title("Flipper Length vs Body Mass")
plt.tight_layout()
plt.show()

# 7.
mean_by_species = df.groupby("species")["body_mass_g"].mean()
median_by_species = df.groupby("species")["body_mass_g"].median()
print(" MEAN BY SPECIES")
print(mean_by_species)
print("MEDIAN BY SPECIES")
print(median_by_species)

# 8. BOX PLOT
plt.figure(figsize=(7, 3))
plt.boxplot(mass_values)
plt.ylabel("Body mass (g)")
plt.title("Body Mass: Spread and Potential Outliers")
plt.tight_layout()
plt.show()