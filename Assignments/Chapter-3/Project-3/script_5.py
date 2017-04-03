#Mortgage Payment Calculator
#Maxwell Phillips
#3 April 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Get and store variables for loan amount, term, and range.
#2)Greeting
#3)Calculate discount
#4)Calculate loan amount using discount value
#5)Print it all out in a pretty table
#6)ask to run again
#-------------------------------------------------------------------------------
#Greeting
print("""
This is a program to calculate the monthly mortgage payment for a given loan
 amount, term (number of years) and range of interest rates from 3% to 18%.
""")
#Begin program loop
terminate = False
print("-"*80)
while (terminate == False):
    #Reset variables
    loan_amount = 0
    loan_term = 0
    #Ask for variables and error check them
    while True:
        try:
            loan_amount = int(input("Please enter a amount for the loan: "))
            break
        except ValueError:
            print("Please enter a positive interger value for the amount of",
            "the loan.")
    while True:
        try:
            loan_term = int(input("Please enter a length for the loan: "))
            break
        except ValueError:
            print("Please enter a positive interger value for the term of",
            "the loan.")
    #Calculate discounts
    n = loan_term * 12
    months_discount = []
    r = 3
    while (r <= 18):
        months_discount.append(int(loan_amount/(((1+r)^n - 1)/r(1+r)^n)))
        r = r + 1
    #Begin printing table
    print("-"*80)
    print("")
    print("loan Amount: "+str(loan_amount)+(" "*10)+"Term: "+str(loan_term)+ " years.")
    print("Interest Rate"+(" "*52)+"Monthly Payment")
    i = 3
    while (i <= 18):
        print(str(i)+"%"+(" "*((len(i)+1)+len(months_discount[i])+len(" Euro.")))+format(months_discount[i], "0.2f")+" Euro.")
    #---------------------------------------
    #Ask to use again
    if(input("\nUse Again (y/n)?: ") == "y"):
        terminate = False
        print("="*80)
    else:
        terminate = True
