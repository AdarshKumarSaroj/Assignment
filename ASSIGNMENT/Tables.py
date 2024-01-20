
def Table(Number):

    try :
        for n in range(10):
            print(f"{Number}  x  {n+1}  =  {Number*(n+1)}")



    except:
        print("Write a Number Not a String")

while True:
    Kk = int(input("Enter : "))
    Table(Kk)