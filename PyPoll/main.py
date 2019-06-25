#import the module
import os
import csv

#define the path for file to open and output file
csvpath = 'election_data.csv'
outputpath = 'PyPoll_Output.txt'

#Variable declaration
count_voters = 0
candidate_name =[]
candidate_count ={}
election_result ={}
sorted_list = []
winner =""

# Read the csv file
with open(csvpath,newline = "") as csvfile:
   csvreader = csv.reader(csvfile)
   csv_header = next(csvreader)

   #Read each row
   for row in csvreader:
       #Add to count voters
       count_voters += 1
       # Save the candidate name in candidatename variable
       candidatename = row[2]

       # Check if candidate name is not present in the candidate_name list
       if candidatename  not in candidate_name:
           # Add the candidate name in candidate_name list
           candidate_name.append(row[2])
           # Reset the candidate_count to zero
           candidate_count[candidatename] = 0
       #if candidate name is already present add it to the candidate_count
       candidate_count[candidatename] += 1

# Export the data to text file
with open(outputpath,"w",encoding ="utf-8") as text_file:
   #print the results in terminal
   print("Election Results")
   print("-------------------------")
   print("Total Votes: ",count_voters)
   print("-------------------------")

   #export the result to text file
   text_file.write("Election Results" +"\n")
   text_file.write("-------------------------" +"\n")
   text_file.write("Total Votes: "+str(count_voters) +"\n")
   text_file.write("-------------------------" +"\n")

   # loop through the candidate_count dictionary and calculate the vote percentage and save it to election_result dictionary
   for i,j in candidate_count.items():
       election_result[i] = round(((float(j)/float(count_voters))*100),5)
       print(i,":",election_result[i] ,"%","(",j,")")
       text_file.write(str(i)+":"+str(election_result[i])+"%"+"("+str(j)+")"+"\n")

   print("-------------------------")
   text_file.write("-------------------------" +"\n")


   # calculate the sorted list of candidate_count dictionary
   sorted_list = sorted(candidate_count.values(),reverse = True)

   #Loop through the candidate_count dictionary
   for key,value in candidate_count.items():

       #look for the key against the value of sorted list in candidate_count dictionary
       if sorted_list[0] == value:
           winner = key
           print("Winner:",winner)

   text_file.write("Winner:" + str(winner))
