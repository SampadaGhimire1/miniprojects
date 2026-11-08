import random
import string
pw=""
pw_len=12
char=string.ascii_letters+string.digits+string.punctuation 
# for i in range(pw_len):
#     pw+=random.choice(char)
# print(pw)
res="".join([random.choice(char) for i in range(pw_len)])
print(res)