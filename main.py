import pandas

def reading_file_with_sep(file_name):
    """
    If the separator between each
     field of your data is not a comma, use the sep argument
    :return: 
    """
    df = pandas.read_csv(file_name, header=0, sep=",")
    return df

def looping_with_iterrows(file_data):
    for index, row in file_data.iterrows():
        print("-------------")
        if row["Header 2"] == "row2field2" and row["Header 3"] == "row2field3":
            print(row["Header 1"])
            print(row)


def looping_with_itertuples(file_data):
    for row in file_data.itertuples():
        print("-------------")
        print("row: {}".format(row))

def main():
    #file_name = "example_with_comma_dot_separator.csv"
    file_name ="example_2.csv"
    df = reading_file_with_sep(file_name)
    looping_with_iterrows(df)

if __name__ == "__main__":
    main()