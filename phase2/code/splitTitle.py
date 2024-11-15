import pandas as pd

# Load the news titles from the text file
df = pd.read_csv("/home/zwang1/cosc426/Final/Dataset/news_title.txt", sep="\t", names=["textid", "text", "condition", "label"])

# Define split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Initialize lists to store split data
train_data = []
val_data = []
test_data = []

# Loop through each unique label and split manually
for label in df["label"].unique():
    # Filter data for the current label
    label_df = df[df["label"] == label].reset_index(drop=True)
    
    # Calculate split sizes
    train_size = int(len(label_df) * train_ratio)
    val_size = int(len(label_df) * val_ratio)
    test_size = len(label_df) - train_size - val_size

    # Perform the manual splits
    train_data.extend(label_df.iloc[:train_size].to_dict("records"))
    val_data.extend(label_df.iloc[train_size:train_size + val_size].to_dict("records"))
    test_data.extend(label_df.iloc[train_size + val_size:].to_dict("records"))

# Convert each split list to a DataFrame
train_df = pd.DataFrame(train_data)
val_df = pd.DataFrame(val_data)
test_df = pd.DataFrame(test_data)

# Reset 'textid' to start from 0 in each DataFrame and set 'condition' to "news"
train_df["textid"] = range(len(train_df))
val_df["textid"] = range(len(val_df))
test_df["textid"] = range(len(test_df))
train_df["condition"] = "news"
val_df["condition"] = "news"
test_df["condition"] = "news"

# Rename 'label' column to 'target' in the test DataFrame
test_df = test_df.rename(columns={"label": "target"})

# Save each DataFrame to a file with the specified format and correct headers
train_df.to_csv("/home/zwang1/cosc426/Final/Dataset/news_title_training.txt", sep="\t", index=False, header=["textid", "text", "condition", "label"])
val_df.to_csv("/home/zwang1/cosc426/Final/Dataset/news_title_validating.txt", sep="\t", index=False, header=["textid", "text", "condition", "label"])
test_df.to_csv("/home/zwang1/cosc426/Final/Dataset/news_title_testing.txt", sep="\t", index=False, header=["textid", "text", "condition", "target"])

print("Data has been split and saved to news_title_training.txt, news_title_validating.txt, and news_title_testing.txt")
