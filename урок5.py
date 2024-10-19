# словари, множества.
# словари

numbers1 = [1, 2, 3, 4, 2, 1, 3, 5]
numbers2 = (1, 2, 3, 4, 2, 1, 3, 5)
numbers3 = {1, 2, 3, 4, 2, 1, 3, 5}
print(numbers1)
print(numbers2)
print(numbers3)

student ={
    'name': 'Azamat', "age": '18'
          }

print(student)

"""доступ к значениям"""

# print(student['name'])
# print(student.'nam'.get())

"""add"""
student['surname'] = 'dairbekov'
student.update({'weiht': 67.4, 'heigtht': 1.17})

"""edit"""
student['age'] = 22

"""delate"""
student.pop('weight')
del student['height']
