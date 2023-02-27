import os
from pathlib import Path
import string
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile
import os

import pandas as pd

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = '311-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)

_setup()

from stop_words import stop_words
from tf_idf import TFIDF


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    text = pd.read_csv("tmp/samples.txt")
    return text


def strip_url_email(x_df):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    x_df.replace("(http|HTTP)(s?|S?):?\/\/(\S+)", "", regex=True, inplace=True)
    x_df.replace("(\S+)@(\S+)", "", regex=True, inplace=True)
    return x_df    


def to_lowercase(x_df):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    x_df = pd.DataFrame(x_df["text"].str.lower())
    return x_df


def strip_stopwords(x_df):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    for index, row in x_df.iterrows():
        x_df.iloc[index]["text"] = " ".join([word for word in row.text.split() if word not in stop_words])
    return x_df


def strip_non_ascii(x_df):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    new_row = ""
    for index, row in x_df.iterrows():
        for char in row.text:
            if char in string.printable:
                new_row += char
        x_df.iloc[index]["text"] = new_row
        new_row = ""
    return x_df


def strip_digits_punctuation(x_df):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters

    new_row = ""
    for index, row in x_df.iterrows():
        for char in row.text:
            if char in string.ascii_letters:
                new_row += char
            elif char == " ":
                new_row += char
            else:
                new_row += ""
        x_df.iloc[index]["text"] = new_row
        new_row = ""
    return x_df
        

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
    x_df = x_df.reindex(sorted(x_df.columns), axis=1)
    return x_df


def get_tdidf():
    # Pandas’ pipeline feature allows you to string together
    #   Python functions in order to build a pipeline of data processing.
    # Complete the functions above in order to produce a 'tf-idf' Dataframe
    # Return the 'tf-idf' Dataframe
    df = (
        load_data()
        .pipe(strip_url_email)
        .pipe(to_lowercase)
        .pipe(strip_stopwords)
        .pipe(strip_non_ascii)
        .pipe(strip_digits_punctuation)
        .pipe(calculate_tfidf)
        .pipe(sort_columns)
    )
    return df