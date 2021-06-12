
#Index No	–	208648J 
#Name		–	R.Seyon 
#Course		–	EN5500 - Computer Systems 
#Submission	–	Analysis of a Data Processing System - 1 


import numpy as np
import statistics

#Creating random array of students marks
marks = np.random.randint(1,101,50)

#finiding the average
average = np.average(marks)

#finiding the standard deviation
std_dev = statistics.stdev(marks)


#creating an array size of 10 for storing the decades
#This is achieved by storing counts of each decade
#in relevant indexes.


#Grouping of distribution    0-9 , 10-19 , 20-29 , 30-39
#                          40-49 , 50-59 , 60-69 , 70-79 ,
#                          80-89 , 90-100

marks_distributions = np.zeros((10,), dtype=int)




for mark in marks:
    decade = mark//10 #Integer division to find the decade
    
    if(decade == 10):
        #if hundred marks
        marks_distributions[9] += 1 #add that to last decade 90-100
    else:
        #lesser than 100
        marks_distributions[decade] += 1 #adding this to relevant decade

print("\n\nMarks of the students of a subject as follows\n")
#Printing marks array
print(marks)

#Printing average and standard deviation
print("\n\nAverage\t\t\t=\t{avg:.2f}\nStandard Deviation\t=\t{sd:.2f}\n\n".format( avg=average , sd=std_dev ))




#printing distributions
for i, md in enumerate(marks_distributions):
    #partucular if else used for alignment because , length of hundred is 3 digit unabled to print in a table format
    if(i==0):
        print("Range\t\t {s} - {e}\t\t<-->\t\tCount : {count}".format(s=i*10 , e=((i+1)*10-1) , count = md))
    elif(i<9):
        print("Range\t\t{s} - {e}\t\t<-->\t\tCount : {count}".format(s=i*10 , e=((i+1)*10-1) , count = md))
    else:
        print("Range\t\t{s} - {e}\t<-->\t\tCount : {count}".format(s=i*10 , e=(i+1)*10 , count = md))


#print line breaker
print("\n\n")


