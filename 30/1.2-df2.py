# Calculate the count of all unique values of a categorical column in a DataFrame.

import pandas as pd

# Example DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

# Calculate count of all unique values
unique_value_counts = df['Category'].value_counts()

print(unique_value_counts)