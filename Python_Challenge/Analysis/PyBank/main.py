#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:21:49 2020

@author: eyris
"""
"Import File"
import os
import csv 
csvpath = os.path.join("Budget_Data.csv")

#Create lists to iterate through
date = []
profit = []
profit_change = []

#Open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        date_count = len(date)
        profit.append(int(row[1]))
        
     

#Calculate Profit Change
    for i in range(len(profit) - 1):
        profit_change.append(profit[i+1] - profit[i])
    
    
#Calculate Total Profit
    Sum = sum(profit)
    
    
#Max & Min Profit Change
max_value = max(profit_change)
min_value = min(profit_change)

max_date = (profit_change.index(max(profit_change))) + 1
min_date = (profit_change.index(min(profit_change))) + 1

#Print Statements
print('Financial Analysis')
print('------------------------------------------------------')
print('Total Months: '+ str(date_count))
print('Total: '+ str(Sum))
print('Average Change: '+ str(round(sum(profit_change)/len(profit_change),2)))
print('Greatest Increase in Profits: '+ date[max_date]+ ' ' + '$'+ str(max_value))
print('Greatest Decrease in Profits: '+ date[min_date]+ ' ' + '$'+ str(min_value))

