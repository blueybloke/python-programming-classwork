#Gift Certificate Dinner Bill Calculator
#Maxwell Phillips
#16 Febuary 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Alogrithm:
#1)Get the value of the gift certificate as a variable
#2)Get the value for person 1's order
#3)Get the value for person 2's order
#4)Calculate and print the total
#5)Calculate and print the tax
#6)Calculate and print the tab
#-------------------------------------------------------------------------------
#Introduction text
print("This program will calculate a resturant tab for a couple with a gift \
certificate, with a resturant tax of 8.0%")
#Store gift certificate value.
gift_cert = float(input("\nEnter the amount of the gift certificate: "))

print("\nEnter the ordered items for person 1:")
appertizer_1 = float(input("Please enter the price for the appertizer: "))
entree_1 = float(input("Please enter the price for the entree: "))
drinks_1 = float(input("Please enter the price for the drinks: "))
dessert_1 = float(input("Please enter the price for the dessert: "))

print("\nEnter the ordered items for person 2:")
appertizer_2 = float(input("Please enter the price for the appertizer: "))
entree_2 = float(input("Please enter the price for the entree: "))
drinks_2 = float(input("Please enter the price for the drinks: "))
dessert_2 = float(input("Please enter the price for the dessert: "))

total= float(appertizer_1+appertizer_2+entree_1+entree_2+drinks_1+drinks_2+ \
dessert_1+dessert_2)
print("\nOrdered Items: $ "+format(total, '0.2f'))
tax= 0.08 * total
print("Resturant tax: $ " + format(tax, '0.2f'))
tab= float((total+tax)-gift_cert)
print("Tab: $ " + format(tab, '0.2f'))
print("(negative amount indicates unused amount of gift certificate.)")
