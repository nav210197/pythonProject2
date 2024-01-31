yr = int(input("Enter the yr"))
if (yr % 4 == 0 and yr % 400 != 0) or yr % 100 == 0:
    print("Entered year is a Leap Year")
else: print("Entered Year is not a Leap Year")