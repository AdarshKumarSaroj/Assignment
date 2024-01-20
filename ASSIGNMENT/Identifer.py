def Leap_Year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main(Year):

    if Leap_Year(Year):
        print(f"\n--->     {Year} : Is a Leap Year\n")

    else:
        print(f"\n--->     {Year} : Is Not a Leap Year\n")



while True:

    a = int(input("\nEnter The Year : "))
    main(a)
