

def Even_And_Odd(data):
    num = int(data)


    if ((num%2)!=0):

        return f"{data} is a Odd Number"

    else:
        return f"{data} is Even Number" 
    


while True:
    try:
        kk = int(input("Enter : "))    
        Ans =Even_And_Odd(kk)
        print(Ans)
    except:

        raise ValueError                 #if the user willnot provide a int input it will raise a error 
    

