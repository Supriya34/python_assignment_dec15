def fname():
    name = str(input("Enter your full name : "))
    namesplit = name.split(' ')

    for i in range(len(namesplit)):
        if i == 0:
            print("First name: {:s}".format(namesplit[0]))
        elif i == len(name_split) - 1:
            print("Last name: {:s}".format(namesplit[len(namesplit)-1]))
        else:
            middle_name = namesplit[i]
            print("Middle name: {:s}".format(middle_name))


fname()
