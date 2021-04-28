'''
Developer: Ömer Ulutürk
Date: 17.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

Find words that are 8 letter long on this text
'''

import re

with open ("question2.txt","r") as file:
    txt=file.read()
    x = re.findall(r"\w{8}", txt)

    for i in x:
        print(i)