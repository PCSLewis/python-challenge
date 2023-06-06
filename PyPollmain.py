import os
import csv

#Set File Path
py_poll_csv = os.path.join("Users\lewis\Desktop\Data Analysis Bootcamp\python-challenge\PyPoll\Resources\election_data_final.csv")

#Output File
output_file = "results.txt"

#Variables
total_votes = 0
votes_per_candidate = {}
candidates = []
winner = ""
winner_total_votes = 0


#Open CSV File
with open("election_data_final.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)

#Loop funtion for total vote count
    for row in csvreader:

#Total the vote count
        total_votes += 1

#Find Candidate Name
        candidate_name = row["Candidate"]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            votes_per_candidate[candidate_name] = 1

        votes_per_candidate[candidate_name] = votes_per_candidate[candidate_name] + 1


with open(output_file, 'w') as txt_file:
    election_header = (
        f"Election Results\n"
        f"\n"
        f"---------------\n"
         f"\n")
    txt_file.write(election_header)

    total_votes_prnt = (
        f"Total Votes: {total_votes}\n"
        f"\n"
        f"---------------\n"
        f"\n")
    print(total_votes_prnt)
    txt_file.write(total_votes_prnt)

    for candidate in votes_per_candidate:
        votes = votes_per_candidate[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_total_votes):
            winner_total_votes = votes
            winner = candidate
        voter_print_out = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_print_out)
        txt_file.write(voter_print_out)
        
    election_winner = (
        f"\n"
        f"---------------\n"
        f"\n"
        f"Election Winner: {winner}\n"
        f"\n"
        f"---------------\n")
    print(election_winner)
    txt_file.write(election_winner)