import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Step 1: Load & Inspect
CSV_PATH = 'car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL HEAD ===")
print(df.head(10))

print("\n=== INITIAL SHAPE ===")
print(df.shape)

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== LOCATION VALUE COUNTS ===")
print(df['Location'].value_counts())

# Key issues noted: mixed types in Price, missing values, typos in Location.

# Step 2: Clean Target Formatting (Price)
df['Price'] = df['Price'].replace({r'\$': '', r',': ''}, regex=True).astype(float)
print("\n=== PRICE DATA TYPE ===")
print(df['Price'].dtype)
print("\n=== PRICE SKEWNESS ===")
print(df['Price'].skew())

# Step 3: Fix Category Errors before Imputation
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': pd.NA})
print("\n=== MISSING VALUES AFTER LOCATION FIX ===")
print(df.isnull().sum())

# Step 4: Impute Missing Values
df['Odometer_km'].fillna(df['Odometer_km'].median(), inplace=True)
df['Doors'].fillna(df['Doors'].mode()[0], inplace=True)
df['Accidents'].fillna(df['Accidents'].mode()[0], inplace=True)
df['Location'].fillna(df['Location'].mode()[0], inplace=True)
print("\n=== MISSING VALUES AFTER IMPUTATION ===")
print(df.isnull().sum())

# Step 5: Remove Duplicates
print("\n=== SHAPE BEFORE REMOVING DUPLICATES ===")
before_shape = df.shape
df.drop_duplicates(inplace=True)
after_shape = df.shape
print(f"Dropped duplicates: {before_shape} → {after_shape}")

# Step 6: Outliers (IQR Capping)
def iqr_capping(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    return Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

low_price, high_price = iqr_capping(df['Price'])
low_odometer, high_odometer = iqr_capping(df['Odometer_km'])

df = df[(df['Price'] >= low_price) & (df['Price'] <= high_price)]
df = df[(df['Odometer_km'] >= low_odometer) & (df['Odometer_km'] <= high_odometer)]

print("\n=== SUMMARY AFTER OUTLIER REMOVAL ===")
print(df.describe())

# Step 7: One-Hot Encode Categorical(s)
df = pd.get_dummies(df, columns=['Location'], drop_first=True)
print("\n=== NEW COLUMNS AFTER ONE-HOT ENCODING ===")
print(df.columns)

# Step 8: Feature Engineering
CURRENT_YEAR = 2025
df['CarAge'] = CURRENT_YEAR - df['Year']
df['Km_per_year'] = df['Odometer_km'] / df['CarAge'].replace(0, np.nan)
df['Is_Urban'] = df['Location_Suburb'].astype(int)
df['LogPrice'] = np.log1p(df['Price'])

# Step 9: Feature Scaling (X only)
features_to_scale = ['Odometer_km', 'CarAge', 'Km_per_year']
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

print("\n=== SAMPLE OF SCALED VALUES ===")
print(df[features_to_scale].head())

# Step 10: Final Checks & Save
print("\n=== FINAL INFO ===")
print(df.info())
print("\n=== FINAL MISSING COUNTS ===")
print(df.isnull().sum())
print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

OUT_PATH = 'car_l3_clean_ready.csv'
df.to_csv(OUT_PATH, index=False)
print(f"Cleaned data saved to {OUT_PATH}")