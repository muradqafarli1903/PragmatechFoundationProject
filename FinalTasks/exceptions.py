n=int(input())
while n>0:
    a=input()
    b=input()
    n-=1


    try:
        int(a)/int(b)
    except ZeroDivisionError:
        print("Error code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10:",b)