
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

#creating an array to store grades
grades = [' ']*len(marks)

#Below section used to find marking distributions and grades
for i, mark in enumerate(marks):
    #Finding marks distribution
    decade = mark//10 #Integer division to find the decade
    
    if(decade == 10):
        #if hundred marks
        marks_distributions[9] += 1 #add that to last decade 90-100
    else:
        #lesser than 100
        marks_distributions[decade] += 1 #adding this to relevant decade
        
    #Find and store grades
    if mark >=85:
        grades[i] = 'A+'
    elif 75 <= mark and mark<85:
        grades[i] = 'A'
    elif 70 <= mark and mark<75:
        grades[i] = 'A-'
    elif mark >=65 and mark<70:
        grades[i] = 'B+'
    elif 60 <= mark and mark<65:
        grades[i] = 'B'
    elif 55 <= mark and mark<60:
        grades[i] = 'B-'
    elif 50 <= mark and mark<55:
        grades[i] = 'C+'
    elif 45 <= mark and mark<50:
        grades[i] = 'C'
    elif 40 <= mark and mark<45:
        grades[i] = 'C-'
    elif 35 <= mark and mark<40:
        grades[i] = 'D'
    elif mark<35:
        grades[i] = 'F'



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


#printing marks and grades
print("Grade of Each mark as follows\n")
print("Marks\tGrade")
for i in range(len(marks)):
    print('{}\t{}'.format(marks[i],grades[i]))
        
#print line breaker
print("\n\n\n")

