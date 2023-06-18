import math

#This is a finance calculator with 2 different types of calculations, either an investment or a bond.

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

#User chooses investment type
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n")

#User will be asked to enter the amount
#the interest rate
#the number of years they plan on investing
#if they want simple or compound interest.

if user_choice.lower() == "investment" or user_choice.upper() =="INVESTMENT":
    deposit = float(input("Please enter the amount of money you would like to deposit: \n"))
    interest_rate = float(input("Please enter the interest rate without the percentage sign: \n"))
    years = float(input("Please enter the number of years you plan on investing: \n"))
    interest = input("Please state if you want simple or compound interest: \n")
    #formulae
    r = interest_rate / 100
    P = deposit
    t = years

# Simple interest calculation
    if interest.lower() == "simple" or interest.upper() == "SIMPLE":
        A = (P*(1 + r*t))
        print("Your total simple interest is: " + str(A))

# Compound interest calculation    
    elif interest.lower() == "compound" or interest.upper() == "COMPOUND":
        A = (P * math.pow((1+r),t))
        print("Your total compound interest is: " + str(A))

    else:
        breakpoint

#Bond interest calculation
elif user_choice.lower() == "bond" or user_choice.upper() =="BOND":
    house_value = float(input("Please enter the present value of the house: \n"))
    bond_interest = float(input("Please enter the interest rate: \n"))
    bond_months = float(input("Please enter the number of months the bond will be repaid over: \n"))
    
    #formulae
    P = house_value
    i = bond_interest / 100
    n = bond_months

    repayment = (i * P)/(1 - (1 + i)**(-n))
    print("The total you would have to pay each month is: " + str(repayment))

else:
    print("Your input is invalid")
