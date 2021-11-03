#Input Variables
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

#Calculate the Final Time
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

#Print Output
finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt) #I took away the the the name of the time in space as in altogether, for example: It use to be
#current_time_str into currentTimeStr because it had to match the name of the time as the input they have and put it
#some capital letter on it on line 6 and 7.
