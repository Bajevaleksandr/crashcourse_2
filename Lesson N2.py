def chiotnoenechiotnoe ():
    print ("Nazovi chislo, suchechka!")
    number26=int(input())
    # if number26%2==0: print ("chiotnoe")
    # else: print ("nechiotnoe")
    print ("xAxA")
    print("Nazovi esche odno chislo, suchechka!")
    number27 = int(input())
    print ("Vvedi odin iz etich symvolov: * / + -")
    action=input()
    if action=="*":
        print (number26*number27)
    elif action == "/":
        print(number26 / number27)
    elif action == "+":
        print(number26 + number27)
    elif action == "-":
        print(number26 - number27)
    else: print("Delai chto tebe skazali, ueban!!!")

chiotnoenechiotnoe()

