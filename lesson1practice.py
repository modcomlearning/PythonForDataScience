# Calculating the Simple Interest


# A. PROCEDURE (ALGORITHM)
# Get the principal fom the user
# get the rate from the user
# Get the time from the user

# create variable interest and assign the operation (principal *rate* time)/100
# E,g interest = (principal *rate* time)/100
# Output the value of interest using print function


# B. SOURCE CODE (PROGRAM)

principal = int(input("Enter the Amount Deposited(Principal) : "))
rate = float(input("Enter the rate of the interest in two decimal places: "))
time = int(input("Enter the time/duration  for the deposit: "))

interest = (principal *rate* time)/100
print(f'The interest of depositing {principal} at the rate of {rate} percent per year in {time} years time is {interest}')

