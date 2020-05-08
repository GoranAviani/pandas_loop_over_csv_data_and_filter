import pandas
def main():
    df = pandas.read_csv('example.csv')
    for index, row in df.iterrows():
        print("index {}, row: {}" .format(index, row))


if __name__ == "__main__":
    main()