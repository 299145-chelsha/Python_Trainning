python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}

'''All course doing students'''
all_course = python_students | java_students | cpp_students
print("All course doing", all_course)

'''Only python students'''
print(python_students.difference(java_students,cpp_students))

'''Both python and jave'''
both = python_students & java_students
print(both)

'''Either python or java)'''
print(python_students ^ java_students)

'''Unique students join in course'''
print(python_students.union(java_students, cpp_students))

'''IN java or cpp not in python'''
print(java_students.union(cpp_students)-python_students)

'''Check all python students in java '''
print(python_students.intersection(java_students))

'''Add Jones to python'''
python_students.add("Jones")
print(python_students)


'''Remove Frank from java set'''
java_students.remove("Frank")
print(java_students)

'''Clear the cpp_students set'''
cpp_students.clear()
