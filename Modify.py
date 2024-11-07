import pandas as pd

# Load the .tsv file into a DataFrame
df = pd.read_csv('news_training_data.tsv', sep='\t')


df = df.rename(columns={"": "label"})


df.to_csv('news_training_data.tsv', sep='\t', index=False)

