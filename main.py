print("Welcome to the tip calculator.")
rawtotal = (input("What was the total bill? $"))
total = (float(rawtotal))
rawpercent = (input("What percentage tip would you like to give? 10, 12, or 15? "))
percent = (float(rawpercent))
rawsplit = (input("How many people to split the bill? "))
split = (float(rawsplit))

pretip = (total / split) 
tip = (pretip * (percent / 100))
share = pretip + tip
myshare = (float(share))
print(f"Each person should pay: ${round(myshare, 2)}")



#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
