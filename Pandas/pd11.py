import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal','nana','nini','nani','nenu','nunu','nono'],
    'Age': [20, 22, 22, 20, 23, 21, 24, 25, 26, 27, 28],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc', 'be', 'msc', 'bca', 'mtech', 'bsc', 'be'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5, 88.5, 82.5, 90.5, 78.5, 68.5, 92.5]
}

df = pd.DataFrame(data)

print(df.info())
# Display Dataset Information