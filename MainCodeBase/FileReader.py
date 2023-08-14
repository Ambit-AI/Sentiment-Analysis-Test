#importing libraries
import pandas as pd

# Importing Variables
from GlobalVaraibles import Sentences


#read From CSV file from Annotated Data Sets Folder
def read_csv(filename):
    return pd.read_excel(filename)


def store_conversation_data(df):
    for index, row in df.iterrows():
        conversation_id = row['Conversation ID']
        text = row['Text']
        source = row['Source']

        if source == "user":
            if conversation_id not in Sentences:
                Sentences[conversation_id] = []

        Sentences[conversation_id].append((source, text))

    return Sentences


def print_conversation_data(Sentences):
    for conversation_id, text_dict in Sentences.items():
        print("Conversation ID:", conversation_id)
        for index,(source, text) in enumerate(text_dict, start=1):
            print(f"Line {index} (Source: {source}):", text)
        print()




