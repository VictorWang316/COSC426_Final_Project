import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK sentence tokenizer if not already downloaded
nltk.download('punkt')

# Load the fakenews.csv file
df = pd.read_csv("/home/zwang1/cosc426/Final/Dataset/True/True_complete.csv")

# Initialize an output DataFrame
output_df = pd.DataFrame(columns=["textid", "text", "condition", "label"])

# Define the condition and label for all rows (modify as needed)
condition = "news"
label = 0  # Example label for all entries; modify based on actual labeling needs

# Initialize a counter for textid
textid_counter = 0

# Loop through each title in the dataset
for _, row in df.iterrows():
    # Assuming 'title' column contains the headline text
    title_text = row['title']
    
    # Split the title into sentences (this might result in a single sentence per title)
    sentences = sent_tokenize(title_text)
    
    # Add each sentence to the output DataFrame
    for sentence in sentences:
        new_row = {
            "textid": textid_counter,
            "text": sentence.strip(),
            "condition": condition,
            "label": label
        }
        output_df = output_df.append(new_row, ignore_index=True)
        textid_counter += 1

# Save the output DataFrame to a .txt file in tab-separated format
output_df.to_csv("Fake_titles.txt", sep="\t", index=False)

print("Data has been saved to processed_titles.txt")
