'''Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
Write a function that calculates area_of_circle and perimeter_of_circle.'''
'''def circle_area_parameter(radious):
    pi=3.14
    area=pi*radious*radious
    parameter=2*pi*radious
    return area,parameter
num=input("Enter the radious")
area,parameter=circle_area_parameter(radious)
print(f"Area of circle is{area}")
print(f"Parameter of a circle is{parameter}")'''

'''Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
Check if all the list items are number types. If not do give a reasonable feedback.'''
'''def add_all_nums(l1):
    sum=[]
    for i in l1:
        if isinstance(i,(int,float)):
         sum=sum+i
        else:
            return "Only numbers can be taken"
l1=list(input("Enter the list:"))
print(add_all_nums(l1))'''

'''Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
 Write a function which converts °C to °F, convert_celsius_2_fahrenheit.'''
'''def convert_celsius_fahrenheit(C):
    F = (C*9/5) + 32
    return F
C=int(input("Enter the cel-"))
print(convert_celsius_fahrenheit(C))'''

'''Write a function called check_season, it takes a month parameter and returns 
the season: Autumn, Winter, Spring or Summer.'''
'''def check_season(month):
    if month == ('september')or('october')or('november'):
        return ('Autum')
    if month == ('june')or('jul')or('august'):
        return ('summer')
    if month == ('march')or('april')or('may'):
        return ('spring')
    if month == ('december')or('january')or('february'):
        return 'winter'
month=input("Enter the name of the month-")
print(check_season(month))'''

'''Write a function called calculate_slope which return the slope of a linear equation
def calculate_slpoe(n):'''


'''Quadratic equation is calculated as follows: ax² + bx + c = 0. 
Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.'''
'''def solve_quadratic_eqn(set):'''


'''Declare a function named reverse_list. 
It takes an array as a parameter and it returns the reverse of the array (use loops).'''
'''def reverse_list(array):
    rev_array=[]
    l=len(array)
    for i in range(l):
        if ((l)-1,-1,-1):
            rev_array.append(array[i])
            return rev_array
print(reverse_list([10,20,30,40,50]))'''

'''Declare a function named print_list. It takes a list as a parameter and 
it prints out each element of the list.'''
'''def print_list(li1):
    for i in li1:
        print(i)
li1=input("Enter the list")
print(print_list(li1))'''

'''Declare a function named capitalize_list_items.
 It takes a list as a parameter and it returns a capitalized list of items'''
'''def capitalize_list_items(li1):
    for i in range(len(li1)):
        li1[i]=str(li1[i]).title()
        return li1
print(capitalize_list_items(['jackfruit','mango','pinapple','guave']))'''

'''Declare a function named add_item. It takes a list and an item parameters.
 It returns a list with the item added at the end.'''
'''def add_item(li1):
    li1.append(None)
    return li1
li1=[1,2,3,'Raman']
print(add_item(li1))'''

'''Declare a function named remove_item. It takes a list and an item parameters.
 It returns a list with the item removed from it.'''
'''def remove_item(li1):
    li1.remove(2)
    return li1
li1=[1,2,3,4,'Aman']
print(remove_item(li1))'''

'''Declare a function named sum_of_numbers. It takes a number parameter 
and it adds all the numbers in that range.'''
'''def sum_of_numbers(n):
    add=0
    for i in range(1, n + 1):
        add += i
        return add
print(sum_of_numbers(10))'''

'''Declare a function named sum_of_odds. It takes a number 
parameter and it adds all the odd numbers in that range.'''
'''def sum_of_odds(num):
    add=0
    for i in range(num):
        if i % 2 !=0:
            add=add+i
    return add
print(sum_of_odds(20))'''

'''Declare a function named sum_of_even. It takes a number parameter 
and it adds all the even numbers in that - range.'''
'''def sum_of_even(num):
    add=0
    for i in range(num):
        if i % 2 == 0:
            add = add+i
    return add
print(sum_of_even(20))'''

