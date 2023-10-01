import random
from random import choice
import requests 



def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def invert(text):
    
    text2 = text[::-1]
    
    return text2


    password_help = '!password (lenght)'
    password1 = '!password (lenght)'
    password1 = '!password (lenght)'
    password1 = '!password (lenght)'
    password1 = '!password (lenght)'
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
