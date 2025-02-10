import pandas as pd

# Creating the dictionary
score = {
    'Math': [78, 85, 96, 80, 86],
    'English': [84, 94, 89, 83, 86],
    'Hindi': [86, 97, 96, 72, 83]
}

# Creating the DataFrame
df = pd.DataFrame(score)

# Displaying the DataFrame
print(df)
