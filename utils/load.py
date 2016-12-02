import csv

def load_csv(file_name):
    """
    load csv data into tuple where the first element in  the tuple is the label
    of each field (position, first name, etc.) and the second position holds
    the data for each player
    """

    data = ([],[])

    with open(file_name, 'rb') as csvfile:

        csv_reader = list(csv.reader(csvfile))]

        data[0].append(csv_reader[0])

        for d in csv_reader[1:]:
            data[1].append(d)

        return data
