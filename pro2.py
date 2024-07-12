P = float(input("Enter the principal amount: "))
T = float(input("Enter the time (in years): "))
R = float(input("Enter the interest rate (in %): "))
SI = (P * T * R) / 100
print("Simple Interest: ", SI)
print("Total Amount: ", P + SI)
