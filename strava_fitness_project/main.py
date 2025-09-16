import pandas as pd

# Load dataset
df = pd.read_csv("strava_activities.csv")
print("First 5 rows:")
print(df.head())

# Convert date column
df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")

# Fill missing calories with mean
df["calories"] = df["calories"].fillna(df["calories"].mean())

# Extract useful features
df["year"] = df["start_time"].dt.year
df["month"] = df["start_time"].dt.month_name()
df["day_of_week"] = df["start_time"].dt.day_name()
df["hour"] = df["start_time"].dt.hour

# Pace (min/km)
df["pace_min_per_km"] = df["duration_min"] / df["distance_km"]

print("\nCleaned dataset:")
print(df.head())

# Save cleaned dataset
df.to_csv("strava_cleaned.csv", index=False)
#day2
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")

# Activity distribution
sns.countplot(x="activity_type", data=df)
plt.title("Activity Distribution")
plt.show()

# Distance distribution
sns.histplot(df["distance_km"], kde=True, bins=10)
plt.title("Distance Distribution")
plt.show()

# Calories distribution
sns.histplot(df["calories"], kde=True, bins=10)
plt.title("Calories Distribution")
plt.show()
