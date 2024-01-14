import os
import csv

#we need to first establish the connection to the files we are using
#This saves the output to file Path to the data csv
csv_path = os.path.join('resources','election_data.csv')
#This saves the output file writing to
Output_path = os.path.join('analysis','pollresults.txt')
#have the file open and set reader so we can loop through data
with open(csv_path) as csvfile:
    csv_reader= csv.reader(csvfile, delimiter =',')
    csv_header = next(csv_reader) #need it because there is a header in the CSV file, this skips it

    #Initialize the counters for the data needed to print
    #Xpert learning Assistant 
    total_votes= 0 #keeps track of all vote counts
    votes= {} #dictionary to store votes for candidates; Candidate=key, value=votes Dictionary={key:value,value,value...}

    #initiate the loop to iterate through all rows in the csvsfile
    for row in csv_reader:
        total_votes += 1 #+1 because all rows represent one vote; use the +- operator to add in all loops
        name= row[2] #candidate names are in column 3

        #Find the votes per candidate
        if name in votes:    #checks if name is in the dictionary "votes{}"
            votes[name] += 1 #if the name is added and continuously found. a value is added to the candidate(name)
        else:
            votes[name] = 1 #This is needed to add a candidate once the loop first finds their name. very important to include to build the dictionary correctly
               
    #calculate who won.
    most_votes= 0 #setup a counter to keep track of votes
    #iterates through items/values in votes dictionary setup above
    for candidate, votecount in votes.items(): #candidate =key, value=votes; votecount grabs votes for that candidate
        if votecount > most_votes: 
            most_votes = votecount
            winner = candidate
    elected= f'Winner: {winner}'

    print(f'Total votes: {total_votes}')
    print(elected)

    #Open the file using write mode, specify varaiable to hold contents
with open(Output_path,'w') as csvfile:
       #initialize CSV writer
       csvwriter= csv.writer(csvfile, delimiter= ",")

       #Write rows in order
       #needed to place the for loop for the stats here since it kept erasing the other candidates if placed above
       csvwriter.writerow(["Election Results"])
       csvwriter.writerow(["-------------------------"])
       Totalvotes= f'Total votes: {total_votes}'
       csvwriter.writerow([Totalvotes])
       csvwriter.writerow(["-------------------------"])
       for candidate, ballot in votes.items(): #candidate =key, value=votes; ballot grabs votes for that candidate
            percentage= (ballot/total_votes)*100
            result = f'{candidate}: {percentage:.3f}% ({ballot})' #formatting needed to print correctly
            print(result)
            csvwriter.writerow([result])  # Writes formatted result to the CSV
       csvwriter.writerow(["-------------------------"])
       csvwriter.writerow([elected])
       csvwriter.writerow(["-------------------------"])