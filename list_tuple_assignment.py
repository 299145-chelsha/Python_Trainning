'''Create list called "even" store all the even numbers,in the range of 1 to 20'''
even = []
for i in range(1 , 21):
    if i % 2 == 0:
        even.append(i)
        print(even)

'''Create list called "odd" , store all the odd numbers in the range from 1 to 20'''
odd = []
for i in range(1 , 21):
    if i % 2 != 0:
        odd.append(i)
        print(odd)

'''Take even and odd list from previous solution merge it in new list called numbers and sort it'''
even = []
odd = []
for i in range(1 , 21):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        a = even + odd
        print("Merged lise", a)

'''Create a nested list called "students" for 5 students, each index store the student info.'''
students = [["Chels", 1, 75],["Arun", 2, 76.4],["Megha", 3, 80],["Bindu", 4, 55.8],["Manav", 5, 66.9]]

'''Write a python program to find the second largest number in a list'''
l1 = [12,23,45,34,27,55]

'''Wap to print unique element from list . ex ...num = [4,3,5,6,3,4,6]'''
l = [4,3,5,6,3,4,6]
for i in l:
    if l.count(i) == 1:
        print(i)

'''Given a tuple of numbers, find the max and min elements.
  ex.. tup = (11,26,45,23,15,18)'''
tup = [11,26,45,23,15,18]
maximum = tup[0]
minimun = [0]
for num in tup:
    if num > maximum:
        maximum = num
        if num < minimum:
            minimum = num

'''Retrieve the 'G' from following list using positive indexing
       L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]'''
L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
print(L1[3][2][2][1][1])

'''WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
       L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]'''
L2= [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

'''WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
      s2 = 'Hello I am going to Bengaluru How are you doing?'''
s2 = 'Hello I am going to Bengaluru How are you doing?'
reverse_Bengaluru = s2[-20:-29:-1]
print(reverse_Bengaluru)





