totalBill = int(input('What was the total bill? $'))
tip = int(input('How many tips did you given to the waitress? $'))
peopleinBill = int(input('How many people? '))
divideBill =  (totalBill + tip) / peopleinBill
print(f'Total bill that each people have to pay ${divideBill}')