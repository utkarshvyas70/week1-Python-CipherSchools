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

language="python"
print(language[-5])

print(language[2:2])
print(language[-3:6])
print(language[:3])

print("Utkarsh"[::-1])

# Excercise 3
name=input("enter your name: ")
print(f"reverse of your name is {name[::-1]}")

name="Utkarsh vyas"
length=len(name)
print(length)
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))

# Excercise 4
name.char=input("enter comma seperated name and character: ").split()
print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")

name="   Utka      rsh"
dots="..........."
print(name+dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ","")+dots)

string="she is beautiful and she is good dancer"
print(string.find("is","was",2))
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)

name=input("enter your name: ")
print(name.center(len(name)+8, "*"))

string="string"
new_string=string.replace('t','T')
print(new_string)

name="utkarsh"
name+="it"
print(name)
age=23
age -=2
print(age)

name="utkarsh"
print(name[-1])
print(name[-1:0:-1])


age=int(input("enter your age: "))
user_name,age=input("enter your name and age: ").split(",")
print(user_name)
print(age)
print(len(name))
print(name.title())
r_pos=(name.title())
r_pos2=name.find("r",r_pos+1)
print(r_pos2)
print(name.center(1,"*"))

age=input("enter your age: ")
age=int(age)
if age>=14:
    print("you are above 14")