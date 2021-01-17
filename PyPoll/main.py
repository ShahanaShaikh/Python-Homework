import os
import csv

PyPoll = os.path.join("Resources/PyPoll_election_data.csv")

voter_id = []
candidates = {}
percentage_of_votes = []

candidates = {"candidate" : "Khan",
              "candidate" : "Correy",
              "candidate" : "Li",
              "candidate" : "O'Tooley"}


with open(PyPoll) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csvreader: 
      voter_id.append((row [0]))

print(f'total number of votes {len(voter_id)}')



