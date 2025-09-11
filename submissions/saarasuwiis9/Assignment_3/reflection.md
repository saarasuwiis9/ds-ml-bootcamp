Reflection on Data Preprocessing Steps

Load & Inspect: I loaded the dataset to understand its structure and identify issues like mixed data types in the Price column and missing values, which are crucial for data cleaning.

Clean Target Formatting (Price): I removed currency symbols and commas from the Price column to convert it into a numeric format, enabling accurate calculations.

Fix Category Errors: I corrected typos in the Location column and converted unknown values to missing values (NaN) to ensure consistency and accuracy in categorical data.

Impute Missing Values:

For Odometer_km, I used the median due to its robustness against outliers.
For Doors and Accidents, I employed the mode to fill in missing values, reflecting the most common occurrences in categorical data.
Remove Duplicates: I eliminated duplicate rows to maintain data integrity and avoid skewed analysis.

Outliers (IQR Capping): I applied IQR capping to the Price and Odometer_km columns to remove extreme values while preserving the overall data distribution.

One-Hot Encoding: I transformed the Location column into binary columns for machine learning compatibility.

Feature Engineering: I created new features:

CarAge: To assess depreciation.
Km_per_year: To indicate annual usage patterns.
Is_Urban: To differentiate urban and rural pricing influences.
LogPrice: To normalize the price distribution for better analysis.
Feature Scaling: I standardized continuous features to ensure they contribute equally to model training, which is important for algorithms sensitive to feature scales.

Final Checks: I confirmed no remaining missing values and saved the cleaned dataset for future analysis.