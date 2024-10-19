# логичиский тип данных. Операторы:условные, сравнения, логические.

rounds = int(input("сколько кругов нужно?:"))
while rounds > 0:
    time = input(f"enter time:({rounds}) ").lower()
    if time in "exit stop выход":
        break
    elif time == "утро" or time == "morning":
        print("доброе утро")
    elif time == "день" or time == "day":
        print("добрый день")
    elif time == "вечер" or time == "evening":
        print("добрый вечер")
    else:
        print("здраствуйте!(время суток неизвестно)")
    rounds -= 1


"""логические операторы"""
# and or not
# print(2 > 3 or 2 < 3)
# print(2 > 3 and 2 > 3)
# print(not False)
# print(not True)

"""операторы сравнения"""
# print(2 == 3)
# print(2 != 3)
# print(2 > 3)
# print(2 < 3)
# print(2 <= 3)
# print(2 >= 3)

# temperature = int(input("enter temperature:"))
#
# if temperature >= -30 and temperature <= 0:
#     print("холодно")
# elif temperature >= 1 and temperature <= 15:
#     print("прохладно")
# elif temperature >= 16 and temperature <= 25:
#     print("тепло")
# elif temperature >= 26 and temperature <= 40:
#     print("жарко")
# else:
#     print(f"несовместимая с жизнью температура - {temperature}")
#

