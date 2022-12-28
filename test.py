import os
from random import choice

file_list = os.listdir('assets/PNG/Square')

print(choice(file_list))
