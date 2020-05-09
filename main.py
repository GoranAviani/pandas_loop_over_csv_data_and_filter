import pandas
def looping_with_iterrows(file_data):
    for index, row in file_data.iterrows():
        print("index {}".format(index))
        print("-------------")
        print("row: {}".format(row))
def looping_with_itertuples(file_data):
    for row in file_data.itertuples():
        print("-------------")
        print("row: {}".format(row))

def main():
    df = pandas.read_csv('example.csv')
    looping_with_itertuples(df)

if __name__ == "__main__":
    main()