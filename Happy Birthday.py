def question1():
    str=input("Can you answer a few my questions?")

    if str=="yes":
      print("Great!")

def happy_birthday():
    str=input("Is your birthday today? Please answer to all the questions yes or no.")

    if str=="yes":
        print ("Good news!")

def presents():
    str=input("Do you have some presents now?")

    if str=="no" or str=="yes":
        print("Ok, now ms.Robot Sonya will give you one.")

def python():
    str=input("Do you want to programming in python?")

    if str=="yes":
        print("SO NICE! Ask my assistant to provide you to the gift!")
    if str=="no":
        print("I think you have a mistake and you wanted to write yes, isn`t it? let`s try again.")
        print("Do you want ot programming in python?")
        print("I knew it! Ask my assistant to provide you to the gift!")


def question2():
    str=input("Ok i`m talking so much, i have one more question to you, is it ok?")

    if str=="yes" or str=="ok":
        print("")


print("Hi, what do you feel right now?")
print("I think you feel yourself good, so, let`s start.")
question1()
happy_birthday()
print("Happy Birthday!")
question2()
presents()

python()

