'''
Developer: Ömer Ulutürk
Date: 17.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a program that detects the ID number hidden in a text.
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
er2tr43e
Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6
Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6
'''
import re

txt = input("Enter Your Text:\n")
x = re.search(r"\w{2}\d\w{2}\d{2}\w\d", txt)


if x:
  print(x.group())
else:
  print("No match")