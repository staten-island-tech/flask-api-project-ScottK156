def divide(a,b):
    try:
        #try something
        result = a/b
    except ZeroDivisionError:
        print("Error can't divide by zero")
    else:
        print(result)
divide(10,0)