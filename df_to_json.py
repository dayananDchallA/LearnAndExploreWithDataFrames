import pandas as pd
  
# initialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
  
# Create DataFrame
df = pd.DataFrame(data)

list_of_jsons = df.to_json(orient='records', lines=True).splitlines()

print(list_of_jsons)