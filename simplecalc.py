from Functions import * 

print("Enter your choice:add,sub,mul,div")

a = input("Enter the operation: ")

num1 = int(input("Enter the value for num1: "))
num2 = int(input("Enter the value for num2: "))

if a.lower()=='add' or a.lower()=='addition':
    print(f"The addition value of {num1} and {num2} is",add(num1,num2))

elif a.lower()=='sub':
    print(f"The sub value of {num1} and {num2} is",sub(num1,num2))

elif a.lower()=='mul':
    print(f"The mul value of {num1} and {num2} is",mul(num1,num2))

elif a.lower()=='div':
    print(f"The div value of {num1} and {num2} is",div(num1,num2))

else:
    print("Invalid Operation")