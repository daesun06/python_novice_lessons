def section_5_solution_1():
    # Write your solution here

    money = 2000
    if money > 1000:
        print("I'm rich!!")
    else:
        print("I'm not reach!!")
        print("But I might be later...")

    # I cannot understand where is the problem.


section_5_solution_1()


def section_5_solution_2():
    # Write your solution here

    # 0 1 = 0 + 1 = 1
    # 0 1 = 0 * 1 = 0
    # errors, using AND and OR conditionals, using elif instead of else
    twinkies = 60
    if twinkies < 100:
        print("That's to few!")
    elif twinkies > 500:
        print("That's to many!")


section_5_solution_2()


def section_5_solution_3(money: int):
    # Write your solution here
    # Deson's code
    # money=2500
    # if money > 1000:
    #     print("That's to many!")
    # else:
    #     print("That's to few!")

    if money >= 100 and money <= 500 or money >= 1000 and money <= 5000:
        return True

    return False


print(section_5_solution_3(99))
print(section_5_solution_3(1250))
print(section_5_solution_3(5001))


def section_5_solution_4(ninjas: int):
    # Write your solution here

    # ninjas=16
    # if ninjas < 30 or ninjas < 50:
    #     print("I can take them!")
    # elif:
    #     print("It will be hard, but I can take them.")

    if ninjas < 10:
        print("Thats too many!")
    elif ninjas < 30:
        print("It'll be a strugle bla bla")
    elif ninjas < 50:
        print("I can fight those ninjas!")


section_5_solution_4(48)  # Thats too many
section_5_solution_4(24)  # Itll be a struggle
section_5_solution_4(6)  # I can fight those ninjas


def section_6_solution_1():
    # Write your solution here
    for i in range(0, 20):
        print(i)
        if i < 9:
            break


section_6_solution_1()


def section_6_solution_2(age: int):
    # Write your solution here

    # I don't understand what to do after
    is_even = age % 2 == 0  # True
    for number in range(1, age + 1):
        # number = 1
        number_is_even = number % 2 == 0  # False
        if is_even:
            # print all even
            if number_is_even:
                print(number)
        else:
            # print all odd
            if not number_is_even:
                print(number)


section_6_solution_2(10)  # 2 4 6 8 10
section_6_solution_2(11)  # 1 3 5 7 9 11

# if {condition} => always returns Boolean :
# if will execute if condition == True


def section_6_solution_3():
    # Write your solution here

    ingredients = ["salad", "tomato", "cheese", "meat", "bread"]

    # print(ingredients[2])
    # Solution 1
    # counter = 0
    # for d in ingredients:
    #     print(counter, d)
    #     counter = counter + 1

    # Solution 2 , optimized
    for i in range(0, len(ingredients)):
        print(i, ingredients[i])


section_6_solution_3()


def section_6_solution_4(earth_weight: int):
    # Write your solution here

    counter = 0
    for w in range(0, 15):
        moon_weigth = (earth_weight + counter) * 0.165
        counter = counter + 1
        print(moon_weigth)


section_6_solution_4(47)


# section_6_solution_1()