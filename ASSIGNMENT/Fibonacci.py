
def Fibonacci(x):

    a,b = 0 ,1 

    for _ in range(x):
        print(a , end=" , ",)
        a,b = b, a+b
    

kk = int(input("Enter : "))

print(Fibonacci(kk))