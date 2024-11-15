import pandas as pd

# File paths
fake_file = "/home/zwang1/cosc426/Final/Dataset/Fake/Fake_complete.csv"
true_file = "/home/zwang1/cosc426/Final/Dataset/True/True_complete.csv"
satire_file = "/home/zwang1/cosc426/Final/Dataset/Satire/satire_titles.txt"
output_file = "/home/zwang1/cosc426/Final/Dataset/news_title_training.txt"

# Initialize an empty list to store title data
data = []

# Initialize textid counter
textid_counter = 0

# Load Fake titles and append to data list with label 1
fake_df = pd.read_csv(fake_file)
for title in fake_df['title']:
    data.append((textid_counter, title.strip(), "news", 1))
    textid_counter += 1

# Load True titles and append to data list with label 0
true_df = pd.read_csv(true_file)
for title in true_df['title']:
    data.append((textid_counter, title.strip(), "news", 0))
    textid_counter += 1

# Load Satire titles and append to data list with label 2
with open(satire_file, 'r', encoding='utf-8') as f:
    satire_titles = f.readlines()
for title in satire_titles:
    data.append((textid_counter, title.strip(), "news", 2))
    textid_counter += 1

# Convert data to a DataFrame
output_df = pd.DataFrame(data, columns=["textid", "text", "condition", "label"])

# Save the output DataFrame to a .txt file in tab-separated format
output_df.to_csv(output_file, sep="\t", index=False)

print(f"Data has been saved to {output_file}")
