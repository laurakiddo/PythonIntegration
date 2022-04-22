import io
import re

def countchars(inputString):
    return len(inputString)

def countwords(inputString):
    return len(re.findall(r'\w+', inputString))

def find_Evenodd(num):
    if(num%2==0):
         print(num," Is an even")
    else:
         print(num," is an odd")