'''Declare a function named evens_and_odds. It takes a positive integer as parameter and
 it counts number of evens and odds in the number.'''
'''def evens_and_odds(num):
    even_count=0
    odd_count=0
    for i in range(num):
        if i % 2 ==0:
            even_count = even_count+i
        else:
            odd_count = odd_count+i
            return even_count,odd_count
n=int(input("enter the numbers:"))
print("even and odd number count",evens_and_odds(n))'''


'''Call your function factorial, it takes a whole number as a parameter
 and it return a factorial of the number'''
'''def find_factorial(num):
    factorial=1
    if num != 0:
        if num == 0:
            return 1
        for i in range(num,1,-1):
            factorial*=i
        return factorial
print(find_factorial(4))'''

'''Call your function is_empty, it takes a parameter and it checks if it is empty or not'''
'''def is_empty(para):
    for i in para:
        if i not in para:
            return True
        else:
            return False
print(is_empty({}))'''

'''Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, 
calculate_range, calculate_variance, calculate_std'''
