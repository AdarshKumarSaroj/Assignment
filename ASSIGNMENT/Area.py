# We can Use math Module but i don't have enough knowledge for that for now 
'''
In this code we have discribed that there are three functions in this code 
 1.  Area of Tringle 
 2.  Area of Rectangle
 3.  Area of Circle

 and The last function "Check" it handle the all data to Know which of the function should Be work 
'''

def Area_Of_Triangle(base , Height):

    Area = 1/2*(base * Height)

    return Area

def Area_Of_Rectangle(length , width):
    Area  = (length * width)

    return Area

def Area_Of_Circle(radius):
    Area = (22/7)*(radius**2)

    return Area


def Check(Data):
    if "a" in Data:
        base = int(input("Enter The Triangle Base : "))
        Height = int(input("Enter The Triangle Height : "))
        print(f"-->     {Area_Of_Triangle(base=base , Height=Height)}")

    if "b" in Data:
        length = int(input("Enter The Rectangle Length : "))
        width = int(input("Enter The Rectangle Width : "))
        print(f"-->     {Area_Of_Rectangle(length=length , width=width)}")

    if "c" in Data:
        radius = int(input("Enter The Radius Of Circle :"))
        print(f"-->     {Area_Of_Circle(radius=radius)}")


print('''
                Press "A" For Area Of Triangle......
                Press "B" For Area Of Rectangle......
                Press "C" For Area Of Circle.......''')
print()
print()
print()

while True:
    kk = str(input("Enter : ")).lower()
    Check(kk)