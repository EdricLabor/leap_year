
year = int(input("Enter a four digit year : "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap yer")
else:
    print(year, "is not a leap year")