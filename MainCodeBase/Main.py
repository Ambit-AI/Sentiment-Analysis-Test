from FileReader import read_csv, store_conversation_data, print_conversation_data
from GlobalVaraibles import Sentences, Number_of_Sentences


def main():
    csv_filename = "../Sentiment-Analysis-Main/AnnotatedDataSets/Tower_Sentiment.xlsx"
    
    df = read_csv(csv_filename, Number_of_Sentences)
    Sentences = store_conversation_data(df)
    print_conversation_data(Sentences)


if __name__ == "__main__":
    main()