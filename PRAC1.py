'''students_info = {'student_names': ['Anil', 'Jayansh', 'Shanvika'],
                 'ages': [19, 4, 7],
                 'roll_nos': (201, 202, 205),
                 'classes': ['Intermediate', 'UKG', '2nd Grade'],
                 'sections': ['A', 'E', 'G'],
                 'percentages': [65.6, 78.9, 99.1]
                 }
print(students_info['ages'][-1:-3:-1])'''

'''subjects = ["python","java","C++","python","javascript","java","python","java","C++","C"]
my_set = set(subjects)
print(my_set)
print(len(my_set))'''

'''object ={table : "a piece of furniture", "list of facts & figures"
    cat : "a small animal"'''
'''even = []
odd = []
for i in range(21):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        a = even + odd
    print("Even and odd num is ", even , odd)'''

"""palindrom"""
'''s=input("Enter the string")
if s == s[::-1]:
    print("Palindrom")
else:
    print("Not palindrom")'''


"""anagram"""
str1=input("Enter the str:")
str2=input("Enter the str2:")
if sorted(str1)==sorted(str2):
    print("Anagram")
else:
    print("Not anagram")