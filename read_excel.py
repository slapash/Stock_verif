import pandas as pd


#préciser le type de dataframe dtype={'':str} en string pour avoir les bons isbn

def isbn_file_read(file):
    df = pd.read_excel(file, dtype={'ISBN':str})

    df = df[df['ISBN'].notna()]

    df = df["ISBN"]



    return df.tolist()

