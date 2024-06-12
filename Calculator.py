def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
        print("division by zero")
    else:
        return x/y

def main():
    num1=float(input("enter the value:"))
    num2=float(input("enter the value:"))
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVISION")
    print("5.MODULUS")
    n=int(input("enter the choice you want:(1,2,3,4,5)"))
    if n==1:
        print(add(num1,num2))
    elif n==2:
        print(subtract(num1,num2))
    elif n==3:
        print(multiply(num1,num2))
    elif n==4:
        print(division(num1,num2))
    else:
        print("invalid input please give number between (1-5)")
        
main()
        