loan_value=int(input("enter the loan value: "))
years=int(input("enter number of years: "))

installment=(loan_value + (loan_value*0.12*years))/(12*years)
print(f"monthly installment is {installment} EGP")