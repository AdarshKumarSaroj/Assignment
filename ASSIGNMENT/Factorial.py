
def factorial(n):
    
    if (n==0 or n==1):
        return 1
    
    else:
        
        return n*(factorial(n-1))
    
while True:
    pass
    inp = int(input("Enter The Number Whose Factorial you want : "))    
    a =factorial(inp)
    print(f"Factorial Of {inp} Will be : {a}",  flush= True)