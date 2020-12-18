import csv


def isPlayerExist(name):
    with open('tennis_atp-master/atp_players.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        name = name.split(" ")
        first = name[0]
        last = name[1]
        for row in csv_reader:
            if first == row["firstname"] and last == row["lastname"]:
                return True
    return False