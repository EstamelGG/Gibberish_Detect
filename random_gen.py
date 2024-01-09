import string
import random

def generate_random_string(length, if_inclde_punc = 0):
    characters = string.ascii_letters + string.digits
    if if_inclde_punc:
        characters += string.punctuation
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

# 生成一个长度为10的随机字符串
for i in range(1000):
    print(generate_random_string(8, 0))