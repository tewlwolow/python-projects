# This programme says hello and asks for your name.

print("Hello world!")

print("What is your name?")     # asks for their name
my_name=input()

print("Good to meet you, " + my_name)

print("The length of your name is:")
print(len(my_name))

print("What is your age?")      # asks for their age
age_parsed_correctly=False
while not age_parsed_correctly:
    try:
        my_age=input()
        age = str(int(my_age)+1)
        print("You will be " + age +" in a year.")
        age_parsed_correctly=True
    except:
      print("Zjebeales ") 



