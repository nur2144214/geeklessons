# Lambda функции. Обработка исключений.

# lamda_func = lambda n1, n2: n1 + n2
# print(lamda_func(1, 2))
#
# def def_func(a, b):
#     return a + b
#
# print(def_func(2, 3))


# def up_first_letter(word: str):
#     return word.title()
#
# def show_words(some_function, some_list):
#     for element in some_list:
#         print(some_function(element))
#
# cities = ['tokmok', 'bishkek', 'darhan']
#
# show_words(up_first_letter, cities)
#
#
# sorted_cities = sorted(cities, key=lambda word: word[2])
# print(sorted_cities)
#
# filter_cities = list(filter(lambda word: len(word) < 5, cities))
#
# cities_map = list(map(lambda word: word.upper, cities))
# print(cities_map)
#№8
try:
    print(2 * "py")
except:
    print('error found')
else:
    print("ok")
finally:
    print("cheking done!")
t = [1, 2, 3, ]
t = tuple(t)
print(t)