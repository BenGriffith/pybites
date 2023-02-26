import os
from pathlib import Path
import string
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile
import os
import re

import pandas as pd

TMP = Path(os.getenv("TMP", f"{os.getcwd()}/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = '311-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)

_setup()

from tmp.stop_words import stop_words
from tmp.tf_idf import TFIDF


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    text = pd.read_csv("tmp/samples.txt", columns=["text"])
    return text


def strip_url_email(x_df):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    x_df.replace("(http|HTTP)s?:?\/\/(\S+)", "", regex=True, inplace=True)
    x_df.replace("(\S+)@(\S+)", "", regex=True, inplace=True)
    return x_df    


def to_lowercase(x_df):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    x_df = pd.DataFrame(x_df["text"].str.lower())
    return x_df


def strip_stopwords(x_df=None):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    df = pd.DataFrame(
        [
            "i me my myself we our ours ourselves you",
            "i me my myself we our ours ourselves you hello world",
            "lorem ipsum dolor sit amet, consectetur adipiscing elit",
        ],
        columns=["text"],
    )
    for stopword in stop_words:

        for index, row in df.iterrows():
            print(stopword)
            if stopword in row.text:
                pass
                #print(stopword, row.text, sep="|")
                #df.iloc[index]["text"] = row.text.strip(stopword)
        #     print(row)
            #df.at[index, "text"] = row.text.replace(stopword, "")
        # for row in x_df.itertuples():
        #     if row.Index == 0:
        #         continue
        #     x_df.iloc[row.Index] = row.text.replace(stopword, "")
    #print(df)
    #return x_df
    


def strip_non_ascii(x_df):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    pass


def strip_digits_punctuation(x_df):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters
    pass


def calculate_tfidf(x_df):
    # Calculate the 'tf-idf' matrix of the 'text' column
    # Return the 'tf-idf' Dataframe
    tfidf_obj = TFIDF(x_df["text"])
    return tfidf_obj()


def sort_columns(x_df):
    # Depending on how the earlier functions are implemented
    #   it's possible that the order of the columns may be different
    # Sort the 'tf-idf' Dataframe columns
    #   This ensure the tests are compatible
    pass


# def get_tdidf():
#     # Pandas’ pipeline feature allows you to string together
#     #   Python functions in order to build a pipeline of data processing.
#     # Complete the functions above in order to produce a 'tf-idf' Dataframe
#     # Return the 'tf-idf' Dataframe
#     df = (
#         load_data()
#         .pipe(strip_url_email)
#         .pipe(to_lowercase)
#         .pipe(strip_stopwords)
#         .pipe(strip_non_ascii)
#         .pipe(strip_digits_punctuation)
#         .pipe(calculate_tfidf)
#         .pipe(sort_columns)
#     )
#     return df


if __name__ == "__main__":
    # text = load_data()
    # text_no_url = strip_url_email(text)
    # text_lower = to_lowercase(text_no_url)
    # strip_stopwords(text_lower)
    strip_stopwords()