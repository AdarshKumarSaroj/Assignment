


def Negative_or_Positive(n):
    try:
        n = int(n)
    except:
        exit()
    if n<0:
        print(f"{n} : Is a Negative Number...")

    else:
        print(f"{n} : Is a Positive Number....")

while True:
    kkk = int(input("Enter : "))
    Negative_or_Positive(kkk)