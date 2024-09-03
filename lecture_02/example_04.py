# Determine if an input year is a leap year
year =  int(input('Enter a year: '))

divisible_by_100 = (year % 100) == 0
divisible_by_400 = (year % 400) == 0
divisible_by_4 = (year % 4) == 0

# Version  1
# if divisible_by_100:
#     if divisible_by_400:
#         print(f'In {year} February has 29 days')
#     else:
#         print(f'In {year} February has 28 days')
# else:
#     if divisible_by_4:
#         print(f'In {year} February has 29 days')
#     else:
#         print(f'In {year} February has 28 days')

#  Version 2
if (divisible_by_100 and divisible_by_400) or (not divisible_by_100 and divisible_by_4):
    print(f'In {year} February has 29 days')
else:
    print(f'In {year} February has 28 days')
