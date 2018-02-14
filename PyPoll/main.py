import csv

csvfile = "Resources/election_data_2.csv"

votes = 0
winner_votes = 0
total_candidates = 0
max_votes = ["", 0]
coptions = []
cvotes = {}


with open(csvfile) as edata:
    reader = csv.DictReader(edata)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in coptions:
            
            coptions.append(row["Candidate"])

            cvotes[row["Candidate"]] = 1
            
        else:
            cvotes[row["Candidate"]] = cvotes[row["Candidate"]] + 1

    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

    for candidate in cvotes:
        print(candidate + " " + str(round(((cvotes[candidate]/votes)*100))) + "%" + " (" + str(cvotes[candidate]) + ")") 
        cresults = (candidate + " " + str(round(((cvotes[candidate]/votes)*100))) + "%" + " (" + str(cvotes[candidate]) + ")") 
    
cvotes

winner = sorted(cvotes.items()) 

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


