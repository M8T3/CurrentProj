import random
import time

def random_key():
    strength = input("Do you want a strong or weak password?: ")
    weak_codes = ["password", "password123", "123456", "qwerty", "abc123", "passw0rd"]
    if strength == "weak":
        return random.choice(weak_codes)
    else:
        number = int(input("How long do you want your password to be?: "))
        start = time.time()
        symbol = 0
        code = []
        while symbol < number:
            a = str(random.randrange(10))
            b = random.choice('abcdefghijklmnopqrstuvwxyz')
            c = random.choice('abcdefghijklmnopqrstuvwxyz').capitalize()
            d = random.choice('!@#$%&')
            e = [a, b, c, d]
            random.shuffle(e)
            code.append("".join(e))
            symbol += 1

        random.shuffle(code)
        key = "".join(code)
        password = str(key[0:number])
        return password
        end = time.time()
        return end-start


start = time.time()
secret = random_key()
end = time.time()
print('Here is your password: ' + secret)
print(str(end-start) + " seconds is the time it took to produce a password")

