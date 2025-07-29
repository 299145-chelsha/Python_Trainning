'''Write a Python program that takes a string and removes all vowels.'''
'''str = "Elephant is an human friendly animal."
str = list(str)
v = "aeiouAEIOU"
for i in str:
    if i in v:
        str.remove(i)
    print(str)'''

'''Given a string, write a program to count the frequency of each character.'''
'''str1 = "Python is a good programming language."
frequ= {}
for i in str:
    if i in frequ:
        frequ(i) += 1
    else:
        frequ(i) = 1
    print(frequ(i))'''

'''Write a Python program to check if two given strings are anagrams of each other'''
'''s1 =(input("Enter the string1:"))
s2 = (input("Enter string2:"))
s1 = s1.upper()
s2 = s2.upper()
if sorted(s1)==sorted(s2):
    print("Strings are anagrams")
else:
    print("Not anagram")'''


'''Write code to reverse the order of words in a sentence, without using built-in reverse functions'''
'''s1 = "I love Hyderabad so much."
a = s1.split()
rev_sen =(a[::-1])
print(rev_sen)'''

'''Write a Python program to find the longest substring without repeating characters.'''



'''Write a program to check if a string is a palindrome, ignoring spaces and punctuation,'''
'''str1 = (input("Enter a string:"))
str1 = str1.lower()
for char in str1:
    if char.isalnum():
        str1 += char
if str1 == str1[::-1]:
 print("Palindrome")
else:
    print("Not palindrome") '''

'''Write code to convert a string so that the first letter of each word is capitalized (like title case), without using .
with out using Title()'''
str1 = "I love Python so much."
word = str1.split()
result =""
for i in word:
    result += i[0].upper()
print(result.strip())
