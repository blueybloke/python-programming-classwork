#Age In Seconds
#Maxwell Phillips
#23 Febuary 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Program greeting
#2)Get user input
#3)Get current date
#4)Calculate results
#5)Display Results
#-------------------------------------------------------------------------------
#Import datetime module
import datetime

#Program greeting
print("This is a program designed to approximate your age in seconds! :D")
print("If you were born before 1900 terminate this program now as it won't work"
" and you should really be in a hospital.")

#Get user input
print("")
year_birth=int(input("\nPlease enter the year you were born as an integer: "))
month_birth=int(input("\nPlease enter the month you were born as an integer: "))
day_birth=int(input("\nPlease enter the day you were born as an integer: "))

#Calculate seconds in days/years/months
numsecs_day = (24)*(60)*(60)
numsecs_year = (365)*numsecs_day
avg_numsecs_year = ((4*numsecs_year)+numsecs_day)//4
avg_numsecs_month = avg_numsecs_year//12

#Calculate results
numsecs_1990_to_dob = (year_birth - 1900)*avg_numsecs_year + (month_birth - 1)*\
avg_numsecs_month + (day_birth * numsecs_day)

numsecs_1990_to_today = (datetime.date.today().year - 1900) * avg_numsecs_year+\
(datetime.date.today().month - 1) * avg_numsecs_month+\
(datetime.date.today().month * numsecs_day)

age_in_secs = numsecs_1990_to_today - numsecs_1990_to_dob
#Print result
print("\nYou are: "+str(age_in_secs)+" seconds old!")
