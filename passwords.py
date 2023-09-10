import random

password_length = int(input('выберите длину пароля'))
 

allowed_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ''.join(random.choice(allowed_characters) for _ in range(password_length))

print("Сгенерированный пароль:", password)
