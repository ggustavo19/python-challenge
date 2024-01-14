import os
import csv

#This saves the output to file Path to the data csv
csv_path = os.path.join('resources','budget_data.csv')
#This saves the output file writing to
Output_path = os.path.join('analysis','results.txt')

with open(csv_path) as csvfile:
    csv_reader= csv.reader(csvfile, delimiter =',')
    csv_header = next(csv_reader) #need it because there is a header in the CSV file
    
    #Initialize the counters for the data needed to print: Months, Profit/loss,changes, avg changes, Greatest inc and dec
    total_months= 0 
    profit_losses= 0
    prior_pl= 0 #needed as placeholder for prior month
    changes= [] #creating a list to store monthly changes to use to calculate the statistics later 
    all_changes= 0 #holds the summation changes of month vs month calculations
    increase= 0 #will hold the value for the greatest increase over the loop iteration
    decrease= 0 
    inc_month="" #will hold the month for the greatest increase iteration over the loop iteration, avoiding a list buildup:XPlearning assistant
    dec_month=""

    #use the +- operator to add in all loops
    for row in csv_reader:
        total_months += 1 #assumes every row is a new month and counts it as 1
        Pl = int(row[1]) #integer conversion from string - looking for data in column 2; we need this line to keep current month value for changes
        profit_losses += Pl #This is adding up all the total profit/losses

        #Calculate average change between months utilizing my VBA code as reference https://github.com/ggustavo19/VBA-challenge
        #formating and debugging aid from Xpert learning assistant
        if prior_pl != 0: #set to 0 so it can start calculating the monthly changes correctly as soon as we have a prior month value
            change= Pl - prior_pl
            all_changes += change
            changes.append(change) #adding to the chnages list set above
            pchange = (change / prior_pl) * 100 if prior_pl != 0 else 0

            #finding the greatest increase and it's month
            #when the change matches if statement it stores  the value in increase variable and dec_month variable  
            if change > increase: 
                increase = change
                inc_month = row[0]
            #finding the greatest increase and it's month 
            if change < decrease: 
                decrease = change 
                dec_month = row[0]

            #reset previous month value as we did in the VBA reference for the next iteration in the loop
        prior_pl= Pl
        #average calculation using the dictionary of changes we built and summation of all changes in the loop
        #https://pythonguides.com/python-print-2-decimal-places/ ; formating reference
    average_change= all_changes/ (len(changes)) if (len(changes)) > 0 else 0
    formatted_change= round(average_change,2)

    #prints in Terminal only- need this to print in CSV
    print(f"Total Months: {total_months}")
    print(f"Total: ${profit_losses}")
    #print(f"Changes: {changes}")  # Debug print to check the changes list - was not populating due to syntax indentation incorrectly placed inside loop
    print(f'Average Change: ${formatted_change}')
    print(f"Greatest Increase in Profits: {inc_month} (${increase})")
    print(f"Greatest Decrease in Profits: {dec_month} (${decrease})")

    #Writing this over in text to file: Open the file using "write" mode, specify varaiable to hold contents
    with open(Output_path,'w') as csvfile:
       #initialize CSV writer
       csvwriter= csv.writer(csvfile, delimiter= ":")

       #Write rows in order
       csvwriter.writerow(["Financial Analysis"])
       csvwriter.writerow(["----------------------------"])
       csvwriter.writerow(["Total Number of Months", total_months])
       csvwriter.writerow(["Total", f"${profit_losses}"])
       csvwriter.writerow(["Average Change", f"${formatted_change}"])
       csvwriter.writerow(["Greatest Increase in Profits", f"{inc_month} (${increase})"])
       csvwriter.writerow(["Greatest Decrease in Profits", f"{dec_month} (${decrease})"])
