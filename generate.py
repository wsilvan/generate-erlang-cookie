import string
from random import choice

items = list(string.ascii_uppercase)

erlang_cookie = [choice(items) for i in range(0, 30)]

print("+"+"".join(erlang_cookie))