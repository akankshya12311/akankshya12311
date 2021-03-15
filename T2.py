n1=int(input('enter a 1st integer: '))
n2=int(input('enter a 2nd integer: '))
try:
    n3=n1/n2
except:
    print("error! number is not divide by zero")
else:
    print(n3)
