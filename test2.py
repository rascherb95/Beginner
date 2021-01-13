import pandas as pd
import numpy as np
import numpy_financial as npf

car_loan = 17656
car_price = car_loan
interest = 0.0
years = 5

car_payments = np.pmt(rate = interest, nper = years, pv = -car_loan)
print(car_payments)


loan_table = np.zeros((5,6))
loan_table = pd.DataFrame(loan_table)
loan_table.columns = ["Year", "Initial Balance", "Payments",
                      "Interest", "Principal", "Ending Balance"]

# Row 0 and column 0 is our Year 1.
# use iloc[] to loacate that
loan_table.iloc[0,0] = 1
# Initial balance it the car_loan amount
loan_table.iloc[0,1] = car_loan
# car payments are the same we calculated above
loan_table.iloc[0,2] = car_payments
# interest payment is initial balance * interest
loan_table.iloc[0,3] = car_loan * interest
# Priciple is car payment - interest
loan_table.iloc[0,4] = car_payments - (car_loan * interest)
# Ending balance is intial balance - principle
loan_table.iloc[0,5] = car_loan - (car_payments - (car_loan * interest))

for i in range (1,5):
    loan_table.iloc[i,1] = loan_table.iloc[(i-1, 5)]

    loan_table.iloc[i,2] = car_payments

    loan_table.iloc[i,3] = loan_table.iloc[i,1] * interest

    loan_table.iloc[i,4] = car_payments - (loan_table.iloc[i,1] * interest)

    loan_table.iloc[i,5] = loan_table.iloc[i,1] - (car_payments - (loan_table.iloc[i,1] * interest))

loan_table = loan_table.round(2)

print(loan_table)
