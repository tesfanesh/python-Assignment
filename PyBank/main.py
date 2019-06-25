#import the module
import os
import csv


#define the path for file to open and output file
filepath = 'budget_data.csv'
outputpath = 'PyBank_Output.txt'

#Variable declaration
total_months = 0
total_revenue = 0
prev_revenue = 0
change_list =[]
greatest_increase = {}

# Read the csv file   
with open(filepath,newline = "",encoding ="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #Read each row
    for row in csvreader:
        #Add to Total months
        total_months + = 1

        #Add to the total revenue
        total_revenue += int(row[1])

        #Calculate the change in revenue
        change = int(row[1]) - prev_revenue

        #Add the change in revenue to greatest_increase dictionary
        greatest_increase[row[0]] = change

        #store the current value of profit/losses to the prev_revenue
        prev_revenue = int(row[1])

        #Add the change to the change_list list
        change_list.append(change)
    
    #print the values in terminal
    print("Financial Analysis")   
    print("----------------------------") 
    print("Total Months:", total_months)
    print("Total:","$", total_revenue)

    #calculate the average of the change_list list
    average = sum(change_list[1:])/len(change_list[1:])
    print("Average Change:","$",round(average,2))
    
#Export the data to text file
with open(outputpath,"w",encoding ="utf-8") as text_file:
    text_file.write("Financial Analysis" +"\n")
    text_file.write("-------------------------" +"\n")
    text_file.write("Total Months: "+str(total_months) +"\n")
    text_file.write("Total:"+"$"+str(total_revenue) +"\n")
    text_file.write("Average Change:"+"$"+str(round(average,2)) +"\n")
    
    # calculate the sorted list of greatest_increase dictionary
    sorted_list = sorted(greatest_increase.values(),reverse = True)

    #Loop through the candidate_count dictionary
    for key,value in greatest_increase.items():

        #look for the key against the highest value of sorted list in greatest_increase dictionary
        if sorted_list[0] == value:
            Greatest = key
            print("Greatest Increase in Profits:",Greatest,"(","$",value,")")
            text_file.write("Greatest Increase in Profits:"+ str(Greatest)+"("+"$"+str(value)+")"+"\n")  

        #look for the key against the lowest value of sorted list in greatest_increase dictionary
        elif sorted_list[-1] == value:
            smallest = key
            print("Greatest Decrease in Profits:",smallest,"(","$",value,")")
            text_file.write("Greatest Decrease in Profits:"+str(smallest)+"("+"$"+str(value)+")"+"\n")
