print("hello world world")
print("I'm Utkarsh")

print("hello \"world\" world")
print("I \"'m\" utkarsh")

print("line1\nline2\nline3")
print("name\tUtkarsh")
print("this is double backslash\\\\")
print("hell\blo")

print("line A \\n line B")
print("line B \\t line B")
print("this is 4 backslash \\\\\\\\")
print(" \\\" \\\' ")

# Excercise 1

print("this is \\\\ double backslash")
print("these are /\\/\\/\\/\\ mountains")
print("he is\tawesome")
print(" \\\" \\n \\t \\\' ")

print(r"line A \" line B")

print("\U0001F602")
print("\U0001F604")
print("\U0001F618")

print(2+3*4)
print(2/4)
print(4/2)
print(4//2)
print(2//4)
print(2**3)
print(2**0.5)
print(round(2**0.5, 4))
print(3%2)
print((2+3)/2)
print((2+3)*5/2%6)
print(12.5%6)
print(2**3**2)
print(2**9)

user_one_name="Rohit"
userOneName="Mohit"

first_name="Utkarsh"
second_name="Vyas"
full_name=first_name + " " + second_name
print(full_name)

name=input("type your name")
print("hello"+name)
age=input("what is your age? ")
print("your age is "+ age)

number_one=int(input("Enter first number"))
number_two=int(input("Enter  second number"))
total=number_one+number_two
print("total is " + str(total))

number1=str(4)
number2=float("44")
number3=int("33")
print(number2 + number3)

name,age="Utkarsh" , "24"
print("hello "+ name+"your age is "+age)
x=y=z=1
print(x+y+z)

name,age=input("enter your name and age ").split(",")
print(name)
print(age)

name="Utkarsh"
age=24
print("hello" + name + "yoir age is "+ str(age))

print("hello {name} your age is {age}".format(name,age+2))

print(f"hello {name} your age is {age +2}")

# Excercise 2

a=input("enter first number: ")
b=input("enter second number: ")
c=input("enter third number: ")
print(f"average of the number : {(int(a) + int(b)+int(c)) / 3}")