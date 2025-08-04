'''Create an empty dictionary called bird
Add name, color, breed, legs, age to the bird dictionary'''
bird={"name":"Loki","Color":"Green","breed":"parrot","legs":2 ,"age":1}
print(bird)

'''Create a student dictionary and add first_name, last_name, gender, age,
 marital_status, skills, country, city and address as keys for the dictionary'''
student={'first_name':'Aditya','last_name':'Aman','gender':'male','age':20,'marital_sts':'unmarrid','skills':['dancing'],'country':'india','city':'Cuttack'}
print(student)
'''len of the dictionary'''
s1=len(student)
print(s1)
'''Get the value of skills and check the data type, it should be a list'''
print(student['skills'])
'''Modify the skills values by adding one or two skills'''
student['skills'].extend(['singing','painting'])
print(student)
'''Change the dictionary to a list of tuples using items() method'''
tup=tuple(student.items())
print(tup)
'''Delete one of the items in the dictionary'''
del student['age']
print(student)
'''Delete one of the dictionaries'''
bird.clear()
print(bird)
del bird
print(bird)