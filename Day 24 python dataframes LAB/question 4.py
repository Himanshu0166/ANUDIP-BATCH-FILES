import pandas as pd
import numpy as np

# Creating the dictionary with specified data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Creating the DataFrame with index labels
df = pd.DataFrame(exam_data)

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Selecting 'name' and 'score' columns
selected_columns = df[['name', 'score']]

# Printing the DataFrame after selection
print("\nDataFrame after selecting 'name' and 'score' columns:")
print(selected_columns)
