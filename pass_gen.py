import random
from sre_parse import SPECIAL_CHARS

lower = 'abcdefghijklmnopqrstuvwxyz'
upper ='ABCDEFGHIJKLMNOPQRSTUVWXZY'
numbers ='0123456789'

string = lower+upper+numbers+SPECIAL_CHARS

length =8
password ="".join(random.sample(string,length))

print("your password is "+ password)