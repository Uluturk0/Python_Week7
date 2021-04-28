'''
Developer: Ömer Ulutürk
Date: 17.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Write a program that list according to email addresses without email domains in a text.
Example:
Input:
The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.
Then New Yorker article on wind farms...
Output :
franky
sinatra123
'''
import re

txt = "The advencements in biomarine studies franky@google.com with the investments necessary andDavos sinatra123@yahoo.com Then New Yorker article on wind farms..."

email = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", txt)


for i in email:
    word = i.split("@")
    print(word[0])