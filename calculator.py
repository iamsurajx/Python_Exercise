# program to performe calculations between two numbers ::
num1=int(input("Enter first number :"))
num2=int(input("Enter first number :"))

print("Choose (+)for ADD\nChoose (-)for substract\nChoose (*)for multi\nChoose (/)for divided\n ")

opt=input("Enter your choice here :")
if opt == '+':
    add=num1+num2
    print(str(num1) + " + " +str(num2)+" = "+str(add))
    print("Addition of Both numbers is "+str(add))
elif opt == '-':
    add = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(add))
    print("Substraction of Both numbers is " + str(add))
elif opt == '*':
    add = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(add))
    print("Multiplication of Both numbers is " + str(add))
elif opt == '/':
    add = num1 / num2
    print(str(num1) + " / " + str(num2) + " = " + str(add))
    print("Division of Both numbers is " + str(add))
else:
    print("Invalid Choice Retry :")
